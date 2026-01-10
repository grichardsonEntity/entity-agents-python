"""
Sophie Agent - Mobile Developer

Expert in React Native, PWA, iOS, and Android development.
"""

import asyncio
from typing import Optional, List

from ..shared import BaseAgent, TaskResult
from .config import sophie_config


class SophieAgent(BaseAgent):
    """
    Sophie - Mobile Developer

    Specializes in:
    - React Native development
    - Progressive Web Apps
    - iOS/Android native
    - Mobile UX patterns
    """

    def __init__(self, config=None):
        super().__init__(config or sophie_config)

    async def create_component(
        self,
        name: str,
        description: str,
        platform: str = "react-native"
    ) -> TaskResult:
        """Create a mobile component"""
        await self.notify(f"Creating {platform} component: {name}")

        prompt = f"""
Create {platform} component: {name}

**Description:** {description}

**Requirements:**
1. Follow platform patterns ({platform})
2. Touch targets minimum 44pt
3. Accessibility support
4. Responsive to screen sizes
5. TypeScript with proper types

**Structure:**
```
components/{name}/
├── {name}.tsx
├── {name}.styles.ts
├── {name}.test.tsx
└── index.ts
```

**Include:**
- Accessibility props (accessibilityLabel, accessibilityRole)
- Proper touch feedback
- Loading and error states
- Responsive styling
"""

        return await self.run_task(prompt)

    async def setup_pwa(self, project_path: str = ".") -> TaskResult:
        """Set up PWA configuration"""
        await self.notify(f"Setting up PWA: {project_path}")

        prompt = f"""
Set up Progressive Web App at: {project_path}

**Create/Update:**

## 1. Web App Manifest (manifest.json)
```json
{{
  "name": "App Name",
  "short_name": "App",
  "description": "App description",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#212121",
  "theme_color": "#10a37f",
  "icons": [
    {{"src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png"}},
    {{"src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png"}}
  ]
}}
```

## 2. Service Worker (sw.js)
- Cache-first strategy for static assets
- Network-first for API calls
- Offline fallback page

## 3. Registration
- Register service worker in main app
- Handle updates gracefully

## 4. Icons
- List required icon sizes
- Provide favicon guidance

## 5. Testing
- Lighthouse PWA audit checklist
- Offline functionality test
"""

        return await self.run_task(prompt)

    async def implement_offline_support(self, feature: str) -> TaskResult:
        """Implement offline support for a feature"""
        prompt = f"""
Implement offline support for: {feature}

**Strategy:**

## 1. Data Caching
- What to cache locally
- Cache invalidation rules
- Storage mechanism (AsyncStorage, IndexedDB)

## 2. Sync Logic
- Queue offline actions
- Sync when online
- Conflict resolution

## 3. UI Handling
- Offline indicator
- Cached data display
- Pending action feedback

## 4. Implementation

```typescript
// Offline-first data hook
const useOfflineData = <T>(
  key: string,
  fetcher: () => Promise<T>
) => {{
  const [data, setData] = useState<T | null>(null);
  const [isOffline, setIsOffline] = useState(!navigator.onLine);

  useEffect(() => {{
    // Check cache first
    const cached = await storage.get(key);
    if (cached) setData(cached);

    // Try network if online
    if (navigator.onLine) {{
      const fresh = await fetcher();
      await storage.set(key, fresh);
      setData(fresh);
    }}
  }}, []);

  return {{ data, isOffline }};
}};
```
"""

        return await self.run_task(prompt)

    async def optimize_performance(self, app_path: str) -> TaskResult:
        """Optimize mobile app performance"""
        await self.notify(f"Optimizing performance: {app_path}")

        prompt = f"""
Optimize mobile performance for: {app_path}

**Analyze and improve:**

## 1. Bundle Size
- Analyze current bundle
- Identify large dependencies
- Code splitting opportunities

## 2. Rendering
- Unnecessary re-renders
- List virtualization (FlatList)
- Image optimization
- Lazy loading

## 3. Memory
- Memory leaks
- Large data handling
- Cleanup on unmount

## 4. Network
- Request batching
- Caching strategy
- Image compression

## 5. Metrics
- Time to interactive
- First contentful paint
- App size

**Provide:**
- Current baseline metrics
- Specific optimizations
- Expected improvements
- Implementation priority
"""

        return await self.run_task(prompt)

    async def add_push_notifications(self, platform: str = "all") -> TaskResult:
        """Add push notification support"""
        prompt = f"""
Add push notifications for platform: {platform}

**Implementation:**

## 1. Setup
- FCM (Firebase Cloud Messaging) for Android
- APNs for iOS
- Web Push for PWA

## 2. Permission Handling
```typescript
const requestPermission = async () => {{
  const status = await Notifications.requestPermissionsAsync();
  if (status.granted) {{
    const token = await getExpoPushToken();
    await registerToken(token);
  }}
}};
```

## 3. Notification Handling
- Foreground display
- Background handling
- Deep linking from notification

## 4. Server Integration
- Token registration endpoint
- Send notification API

## 5. Testing
- Test on real devices
- Handle edge cases (denied, expired tokens)
"""

        return await self.run_task(prompt)

    async def work(self, task: str) -> TaskResult:
        """General mobile development work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Sophie - Mobile Developer Agent")
    parser.add_argument("--component", type=str, help="Create component")
    parser.add_argument("--description", type=str, help="Component description")
    parser.add_argument("--platform", type=str, default="react-native", help="Platform")
    parser.add_argument("--pwa", type=str, nargs="?", const=".", help="Setup PWA")
    parser.add_argument("--offline", type=str, help="Implement offline for feature")
    parser.add_argument("--optimize", type=str, help="Optimize app performance")
    parser.add_argument("--push", type=str, nargs="?", const="all", help="Add push notifications")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = SophieAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.component and args.description:
        result = await agent.create_component(args.component, args.description, args.platform)
        print(result.output)
        return

    if args.pwa is not None:
        result = await agent.setup_pwa(args.pwa)
        print(result.output)
        return

    if args.offline:
        result = await agent.implement_offline_support(args.offline)
        print(result.output)
        return

    if args.optimize:
        result = await agent.optimize_performance(args.optimize)
        print(result.output)
        return

    if args.push is not None:
        result = await agent.add_push_notifications(args.push)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Sophie - Mobile Developer")
    print("=========================")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
