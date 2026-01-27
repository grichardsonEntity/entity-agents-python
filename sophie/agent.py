"""
Sophie Agent - Mobile Developer

Expert in React Native, PWA, iOS, Android, Wearables, Figma Design Systems, and MCP/AI Integration.
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
    - Figma design systems and tokens
    - Wearables (Apple Watch, Samsung, Garmin, medical devices)
    - Health data integration (HealthKit, Health Connect)
    - MCP and LLM AI agent integration
    - App Store and Play Store compliance
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

    async def setup_figma_integration(
        self,
        figma_file_id: str,
        token_format: str = "style-dictionary"
    ) -> TaskResult:
        """Set up Figma design system integration"""
        await self.notify(f"Setting up Figma integration: {figma_file_id}")

        prompt = f"""
Set up Figma design system integration for file: {figma_file_id}

**Token Format:** {token_format}

**Implementation:**

## 1. Figma Token Extraction
- Connect to Figma API or use MCP Figma server
- Extract design tokens:
  - Colors (primitives and semantic)
  - Typography (font families, sizes, weights, line heights)
  - Spacing (padding, margins, gaps)
  - Border radius
  - Shadows/elevation
  - Breakpoints

## 2. Token Transformation
```javascript
// tokens/colors.json
{{
  "color": {{
    "primary": {{
      "value": "#10a37f",
      "type": "color"
    }},
    "background": {{
      "light": {{ "value": "#ffffff" }},
      "dark": {{ "value": "#212121" }}
    }}
  }}
}}
```

## 3. Style Dictionary Configuration
```javascript
// style-dictionary.config.js
module.exports = {{
  source: ['tokens/**/*.json'],
  platforms: {{
    'react-native': {{
      transformGroup: 'react-native',
      buildPath: 'src/theme/',
      files: [{{
        destination: 'tokens.ts',
        format: 'javascript/es6',
      }}],
    }},
    ios: {{
      transformGroup: 'ios-swift',
      buildPath: 'ios/Theme/',
      files: [{{
        destination: 'StyleDictionary.swift',
        format: 'ios-swift/class.swift',
      }}],
    }},
    android: {{
      transformGroup: 'android',
      buildPath: 'android/app/src/main/res/values/',
      files: [{{
        destination: 'colors.xml',
        format: 'android/colors',
      }}],
    }},
  }},
}};
```

## 4. MCP Figma Integration
```typescript
// Using Figma MCP server
const figmaServer = new MCPClient({{
  server: 'figma-mcp-server',
}});

// Fetch latest tokens
const tokens = await figmaServer.callTool('get_design_tokens', {{
  fileId: '{figma_file_id}',
  includeStyles: true,
  includeVariables: true,
}});
```

## 5. Sync Workflow
- Set up CI/CD pipeline for token sync
- Create PR when tokens change
- Document token usage

## 6. Theme Provider Setup
```typescript
import {{ tokens }} from './theme/tokens';

export const theme = {{
  colors: tokens.color,
  typography: tokens.typography,
  spacing: tokens.spacing,
}};

// ThemeProvider wrapper for app
```

**Deliverables:**
- Token extraction scripts
- Style Dictionary configuration
- Theme provider setup
- Sync automation
- Documentation
"""

        return await self.run_task(prompt)

    async def setup_wearable_integration(
        self,
        platforms: List[str],
        health_categories: List[str]
    ) -> TaskResult:
        """Set up wearable device integration"""
        platforms_str = ", ".join(platforms)
        categories_str = ", ".join(health_categories)
        await self.notify(f"Setting up wearables: {platforms_str}")

        prompt = f"""
Set up wearable integration for platforms: {platforms_str}

**Health Data Categories:** {categories_str}

**Implementation:**

## 1. Platform-Specific Setup

### Apple Watch (watchOS)
```swift
// WatchKit Extension
import HealthKit
import WatchKit

class HealthManager: ObservableObject {{
    let healthStore = HKHealthStore()

    func requestAuthorization() async throws {{
        let typesToRead: Set<HKSampleType> = [
            HKObjectType.quantityType(forIdentifier: .heartRate)!,
            HKObjectType.quantityType(forIdentifier: .stepCount)!,
            HKObjectType.categoryType(forIdentifier: .sleepAnalysis)!,
            HKObjectType.quantityType(forIdentifier: .oxygenSaturation)!,
        ]

        try await healthStore.requestAuthorization(toShare: [], read: typesToRead)
    }}

    func startHeartRateQuery() -> HKAnchoredObjectQuery {{
        // Real-time heart rate monitoring
    }}
}}
```

### Samsung Galaxy Watch (Wear OS)
```kotlin
// Health Connect integration
import androidx.health.connect.client.HealthConnectClient
import androidx.health.connect.client.records.*

class HealthRepository(private val healthConnectClient: HealthConnectClient) {{

    suspend fun readHeartRateRecords(
        startTime: Instant,
        endTime: Instant
    ): List<HeartRateRecord> {{
        val request = ReadRecordsRequest(
            recordType = HeartRateRecord::class,
            timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
        )
        return healthConnectClient.readRecords(request).records
    }}
}}
```

### Garmin (Connect IQ)
```javascript
// Garmin Connect IQ App
using Toybox.Application;
using Toybox.WatchUi;
using Toybox.Sensor;

class GarminHealthApp extends Application.AppBase {{
    function initialize() {{
        AppBase.initialize();
    }}

    function onStart(state) {{
        Sensor.setEnabledSensors([Sensor.SENSOR_HEARTRATE]);
        Sensor.enableSensorEvents(method(:onSensor));
    }}

    function onSensor(sensorInfo) {{
        if (sensorInfo.heartRate != null) {{
            // Process heart rate data
        }}
    }}
}}
```

### Medical Wearables (BLE)
```typescript
// React Native BLE for medical devices
import {{ BleManager }} from 'react-native-ble-plx';

const bleManager = new BleManager();

// Standard BLE Health Device Profile UUIDs
const HEART_RATE_SERVICE = '180D';
const HEART_RATE_MEASUREMENT = '2A37';
const GLUCOSE_SERVICE = '1808';
const BLOOD_PRESSURE_SERVICE = '1810';

async function connectToMedicalDevice(deviceId: string) {{
    const device = await bleManager.connectToDevice(deviceId);
    await device.discoverAllServicesAndCharacteristics();

    // Subscribe to heart rate notifications
    device.monitorCharacteristicForService(
        HEART_RATE_SERVICE,
        HEART_RATE_MEASUREMENT,
        (error, characteristic) => {{
            if (characteristic?.value) {{
                const heartRate = parseHeartRateData(characteristic.value);
                // Process and store data
            }}
        }}
    );
}}
```

## 2. Data Synchronization

```typescript
// Unified health data sync
interface HealthDataSync {{
    syncToServer(data: HealthRecord[]): Promise<void>;
    syncFromDevice(deviceType: DeviceType): Promise<HealthRecord[]>;
    resolveConflicts(local: HealthRecord[], remote: HealthRecord[]): HealthRecord[];
}}

// Background sync service
const backgroundSync = async () => {{
    const healthData = await gatherHealthData();
    await encryptAndUpload(healthData);
    await updateLocalCache(healthData);
}};
```

## 3. Required Permissions & Entitlements

### iOS (Info.plist)
```xml
<key>NSHealthShareUsageDescription</key>
<string>We need access to your health data to track your wellness.</string>
<key>NSHealthUpdateUsageDescription</key>
<string>We need to save workout data to Apple Health.</string>
```

### Android (AndroidManifest.xml)
```xml
<uses-permission android:name="android.permission.health.READ_HEART_RATE"/>
<uses-permission android:name="android.permission.health.READ_STEPS"/>
<uses-permission android:name="android.permission.health.READ_SLEEP"/>
<uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>
```

## 4. Data Privacy & Security
- Encrypt health data at rest and in transit
- Implement secure key storage (Keychain/Keystore)
- HIPAA compliance considerations
- User consent and data deletion workflows

**Deliverables:**
- Platform-specific health integrations
- BLE device connection handling
- Data sync architecture
- Permission handling
- Security implementation
"""

        return await self.run_task(prompt)

    async def setup_health_data_sync(
        self,
        data_types: List[str],
        sync_strategy: str = "bidirectional"
    ) -> TaskResult:
        """Set up health data synchronization"""
        types_str = ", ".join(data_types)
        await self.notify(f"Setting up health sync: {types_str}")

        prompt = f"""
Set up health data synchronization for: {types_str}

**Sync Strategy:** {sync_strategy}

**Implementation:**

## 1. Health Data Models

```typescript
// Unified health data types
interface HeartRateRecord {{
    timestamp: Date;
    bpm: number;
    source: 'apple_watch' | 'samsung' | 'garmin' | 'medical_device';
    deviceId: string;
    context?: 'resting' | 'active' | 'sleep';
}}

interface SleepRecord {{
    startTime: Date;
    endTime: Date;
    stages: SleepStage[];
    source: string;
}}

interface WorkoutRecord {{
    type: WorkoutType;
    startTime: Date;
    endTime: Date;
    calories: number;
    heartRateSamples: HeartRateRecord[];
    distance?: number;
    source: string;
}}
```

## 2. HealthKit Sync (iOS)

```swift
class HealthKitSync {{
    private let healthStore = HKHealthStore()

    func syncHeartRate(from startDate: Date) async throws -> [HeartRateRecord] {{
        let heartRateType = HKQuantityType.quantityType(forIdentifier: .heartRate)!
        let predicate = HKQuery.predicateForSamples(withStart: startDate, end: Date())

        return try await withCheckedThrowingContinuation {{ continuation in
            let query = HKSampleQuery(
                sampleType: heartRateType,
                predicate: predicate,
                limit: HKObjectQueryNoLimit,
                sortDescriptors: [NSSortDescriptor(key: HKSampleSortIdentifierStartDate, ascending: true)]
            ) {{ _, samples, error in
                // Transform to unified format
            }}
            healthStore.execute(query)
        }}
    }}

    // Background delivery for real-time sync
    func enableBackgroundDelivery() {{
        healthStore.enableBackgroundDelivery(
            for: heartRateType,
            frequency: .immediate
        ) {{ success, error in }}
    }}
}}
```

## 3. Health Connect Sync (Android)

```kotlin
class HealthConnectSync(private val client: HealthConnectClient) {{

    suspend fun syncHeartRate(startTime: Instant): List<HeartRateRecord> {{
        val response = client.readRecords(
            ReadRecordsRequest(
                recordType = HeartRateRecord::class,
                timeRangeFilter = TimeRangeFilter.after(startTime)
            )
        )
        return response.records.map {{ it.toUnifiedFormat() }}
    }}

    // Register for changes
    suspend fun registerForChanges() {{
        client.registerForDataNotifications(
            notificationIntentAction = "HEALTH_DATA_CHANGED"
        )
    }}
}}
```

## 4. Server Sync Architecture

```typescript
// Sync service
class HealthSyncService {{
    private queue: SyncQueue;
    private conflictResolver: ConflictResolver;

    async sync() {{
        // 1. Pull server changes
        const serverChanges = await this.api.getChanges(this.lastSyncToken);

        // 2. Get local changes
        const localChanges = await this.localDb.getUnsyncedChanges();

        // 3. Resolve conflicts
        const resolved = this.conflictResolver.resolve(localChanges, serverChanges);

        // 4. Apply changes
        await this.applyToLocal(resolved.serverWins);
        await this.pushToServer(resolved.localWins);

        // 5. Update sync token
        this.lastSyncToken = serverChanges.syncToken;
    }}
}}
```

## 5. Offline Support

```typescript
// Queue offline operations
class OfflineSyncQueue {{
    async queueHealthData(record: HealthRecord) {{
        await this.localDb.insert(record);
        await this.syncQueue.add({{
            type: 'health_record',
            payload: record,
            timestamp: Date.now(),
        }});
    }}

    async processQueue() {{
        const pending = await this.syncQueue.getPending();
        for (const item of pending) {{
            try {{
                await this.api.sync(item);
                await this.syncQueue.markComplete(item.id);
            }} catch (e) {{
                if (!isRetryable(e)) {{
                    await this.syncQueue.markFailed(item.id);
                }}
            }}
        }}
    }}
}}
```

**Deliverables:**
- Unified health data models
- Platform-specific sync implementations
- Conflict resolution logic
- Offline queue system
- Background sync setup
"""

        return await self.run_task(prompt)

    async def setup_mcp_ai_integration(
        self,
        ai_providers: List[str],
        features: List[str]
    ) -> TaskResult:
        """Set up MCP and AI agent integration for mobile"""
        providers_str = ", ".join(ai_providers)
        features_str = ", ".join(features)
        await self.notify(f"Setting up MCP/AI integration: {providers_str}")

        prompt = f"""
Set up MCP and AI integration for mobile app.

**AI Providers:** {providers_str}
**Features:** {features_str}

**Implementation:**

## 1. MCP Client Setup

```typescript
// MCP client for React Native
import {{ MCPClient, Tool, Resource }} from '@anthropic/mcp-sdk';

class MobileMCPClient {{
    private client: MCPClient;
    private serverUrl: string;

    constructor(serverUrl: string) {{
        this.serverUrl = serverUrl;
        this.client = new MCPClient({{
            transport: 'http', // or 'websocket' for real-time
        }});
    }}

    async connect() {{
        await this.client.connect(this.serverUrl);
        const capabilities = await this.client.getServerCapabilities();
        return capabilities;
    }}

    async callTool<T>(name: string, params: Record<string, unknown>): Promise<T> {{
        const result = await this.client.callTool(name, params);
        return result as T;
    }}

    async getResource(uri: string): Promise<Resource> {{
        return this.client.getResource(uri);
    }}
}}
```

## 2. AI Provider Integration

### Claude Integration
```typescript
import Anthropic from '@anthropic-ai/sdk';

class ClaudeService {{
    private client: Anthropic;

    async chat(messages: Message[], tools?: Tool[]): Promise<string> {{
        const response = await this.client.messages.create({{
            model: 'claude-sonnet-4-20250514',
            max_tokens: 1024,
            messages,
            tools, // MCP tools available to Claude
        }});
        return response.content[0].text;
    }}

    async streamChat(messages: Message[], onChunk: (text: string) => void) {{
        const stream = await this.client.messages.stream({{
            model: 'claude-sonnet-4-20250514',
            max_tokens: 1024,
            messages,
        }});

        for await (const chunk of stream) {{
            if (chunk.type === 'content_block_delta') {{
                onChunk(chunk.delta.text);
            }}
        }}
    }}
}}
```

### Gemini Integration
```typescript
import {{ GoogleGenerativeAI }} from '@google/generative-ai';

class GeminiService {{
    private client: GoogleGenerativeAI;

    async chat(prompt: string, context?: HealthContext): Promise<string> {{
        const model = this.client.getGenerativeModel({{ model: 'gemini-pro' }});

        const result = await model.generateContent({{
            contents: [{{ role: 'user', parts: [{{ text: prompt }}] }}],
            systemInstruction: this.buildHealthContext(context),
        }});

        return result.response.text();
    }}
}}
```

## 3. Secure API Key Management

```typescript
// Never store API keys in code or bundle
import * as SecureStore from 'expo-secure-store';
import {{ MMKV }} from 'react-native-mmkv';

class SecureKeyManager {{
    // Store API keys securely
    async storeApiKey(provider: string, key: string) {{
        await SecureStore.setItemAsync(`api_key_${{provider}}`, key);
    }}

    // Retrieve for API calls
    async getApiKey(provider: string): Promise<string | null> {{
        return SecureStore.getItemAsync(`api_key_${{provider}}`);
    }}

    // Or use backend proxy (recommended)
    async getProxiedResponse(provider: string, request: AIRequest) {{
        return fetch('/api/ai/proxy', {{
            method: 'POST',
            body: JSON.stringify({{ provider, request }}),
            headers: {{ Authorization: `Bearer ${{this.userToken}}` }},
        }});
    }}
}}
```

## 4. Health-Aware AI Context

```typescript
// Build context from health data for AI
class HealthAIContext {{
    async buildContext(userId: string): Promise<string> {{
        const recentHealth = await this.healthService.getRecent(userId);

        return `
User Health Context:
- Resting heart rate: ${{recentHealth.restingHR}} bpm
- Average sleep: ${{recentHealth.avgSleep}} hours
- Activity level: ${{recentHealth.activityLevel}}
- Recent trends: ${{recentHealth.trends}}

Use this context to provide personalized health insights.
        `;
    }}

    async analyzeWithAI(query: string, healthData: HealthData) {{
        const context = await this.buildContext(healthData.userId);
        const response = await this.aiService.chat([
            {{ role: 'system', content: context }},
            {{ role: 'user', content: query }},
        ]);
        return response;
    }}
}}
```

## 5. Streaming UI for AI Responses

```typescript
// Real-time AI response display
const AIResponseView: React.FC = () => {{
    const [response, setResponse] = useState('');
    const [isStreaming, setIsStreaming] = useState(false);

    const askAI = async (question: string) => {{
        setIsStreaming(true);
        setResponse('');

        await aiService.streamChat(
            [{{ role: 'user', content: question }}],
            (chunk) => setResponse(prev => prev + chunk)
        );

        setIsStreaming(false);
    }};

    return (
        <View>
            <MarkdownView content={{response}} />
            {{isStreaming && <TypingIndicator />}}
        </View>
    );
}};
```

## 6. Tool Use from Mobile

```typescript
// Let AI use MCP tools
const tools: Tool[] = [
    {{
        name: 'get_health_summary',
        description: 'Get user health summary for date range',
        parameters: {{
            startDate: {{ type: 'string' }},
            endDate: {{ type: 'string' }},
        }},
    }},
    {{
        name: 'log_symptom',
        description: 'Log a health symptom',
        parameters: {{
            symptom: {{ type: 'string' }},
            severity: {{ type: 'number' }},
        }},
    }},
];

// Handle tool calls from AI
async function handleToolCall(toolCall: ToolCall) {{
    switch (toolCall.name) {{
        case 'get_health_summary':
            return await healthService.getSummary(toolCall.params);
        case 'log_symptom':
            return await healthService.logSymptom(toolCall.params);
    }}
}}
```

**Deliverables:**
- MCP client implementation
- Multi-provider AI integration
- Secure key management
- Health-aware context building
- Streaming response UI
- Tool use handling
"""

        return await self.run_task(prompt)

    async def check_store_compliance(
        self,
        platform: str,
        app_type: str = "health"
    ) -> TaskResult:
        """Check app store compliance and provide submission guidance"""
        await self.notify(f"Checking {platform} store compliance")

        prompt = f"""
Perform comprehensive app store compliance check for: {platform}

**App Type:** {app_type}

**Compliance Audit:**

## 1. Apple App Store Review Guidelines

### Required for Health Apps
- [ ] HealthKit entitlement properly configured
- [ ] NSHealthShareUsageDescription in Info.plist
- [ ] NSHealthUpdateUsageDescription if writing data
- [ ] Clear explanation of health data usage
- [ ] Data not used for advertising or sold to third parties

### Privacy Requirements
- [ ] Privacy Policy URL provided
- [ ] App Privacy "nutrition label" completed
  - Data types collected
  - Data linked to user
  - Data used for tracking
- [ ] App Tracking Transparency (ATT) if tracking
- [ ] Purpose strings for all permissions

### Design Requirements
- [ ] Human Interface Guidelines compliance
- [ ] Proper use of system UI elements
- [ ] Accessibility support (VoiceOver)
- [ ] iPad support if universal app
- [ ] Dark mode support

### Technical Requirements
- [ ] Minimum iOS version appropriate
- [ ] No private API usage
- [ ] No crashes on launch
- [ ] Proper error handling
- [ ] Background modes justified

### In-App Purchase (if applicable)
- [ ] Subscriptions follow guidelines
- [ ] Restore purchases implemented
- [ ] Clear subscription terms
- [ ] No external payment links

## 2. Google Play Store Policies

### Health App Requirements
- [ ] Health Connect permissions declared
- [ ] Permissions declared in manifest match usage
- [ ] Sensitive permissions have clear justification
- [ ] Medical disclaimer if providing health advice

### Data Safety Section
- [ ] All data collection disclosed
- [ ] Data sharing practices documented
- [ ] Security practices described
- [ ] Data deletion option provided

### Technical Requirements
- [ ] Target API level meets requirements (currently 34+)
- [ ] 64-bit support
- [ ] Proper permission handling
- [ ] No background battery drain

### Design Requirements
- [ ] Material Design compliance
- [ ] Adaptive icons
- [ ] Proper back navigation
- [ ] Edge-to-edge display support

## 3. Common Rejection Reasons & Prevention

### Apple Rejections
| Reason | Prevention |
|--------|------------|
| Incomplete information | Fill all App Store Connect fields |
| Crashes | Test on all supported devices |
| Broken links | Verify all URLs work |
| Misleading description | Accurate screenshots and description |
| Insufficient permissions justification | Clear usage descriptions |

### Google Rejections
| Reason | Prevention |
|--------|------------|
| Policy violation | Review all policies before submission |
| Deceptive behavior | Accurate listing, no hidden functionality |
| Malicious behavior | No data collection without consent |
| Sensitive permissions | Only request necessary permissions |

## 4. Pre-Submission Checklist

```markdown
### Build Preparation
- [ ] Remove all debug code and logging
- [ ] Verify production API endpoints
- [ ] Test with production certificates
- [ ] Verify analytics are configured
- [ ] Check crash reporting setup

### Store Listing
- [ ] App name (30 chars for iOS, 50 for Android)
- [ ] Subtitle/short description
- [ ] Full description with keywords
- [ ] Screenshots for all device sizes
- [ ] App preview video (optional)
- [ ] Category selection
- [ ] Age rating questionnaire
- [ ] Contact information

### Legal
- [ ] Privacy policy URL (required)
- [ ] Terms of service URL
- [ ] EULA if needed
- [ ] Medical disclaimer for health apps
- [ ] HIPAA compliance if handling PHI

### Testing
- [ ] Beta testing completed (TestFlight/Internal)
- [ ] All user flows tested
- [ ] Edge cases handled
- [ ] Offline behavior verified
- [ ] Permission denial flows tested
```

## 5. Health App Specific Considerations

### FDA Compliance
- Mobile apps that diagnose, treat, or prevent disease may be regulated
- "General wellness" apps have more flexibility
- Document intended use clearly

### HIPAA (if applicable)
- Business Associate Agreement if handling PHI
- Encryption requirements
- Audit logging
- Access controls

### Medical Device Guidance
- Clear disclaimers: "Not a medical device"
- Don't make diagnostic claims without approval
- Refer users to healthcare providers

## 6. Submission Strategy

### Phased Approach
1. **Internal Testing**: Full team testing
2. **Closed Beta**: Limited external users
3. **Open Beta**: Broader audience
4. **Staged Rollout**: Gradual release (Android)
5. **Full Release**: Complete availability

### Review Time Optimization
- Submit early in the week
- Provide demo account credentials
- Include detailed review notes
- Respond quickly to rejections

**Output:**
- Compliance status for each requirement
- Specific items that need attention
- Recommended fixes
- Submission timeline guidance
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
    parser.add_argument("--figma", type=str, help="Setup Figma integration with file ID")
    parser.add_argument("--token-format", type=str, default="style-dictionary", help="Token format for Figma")
    parser.add_argument("--wearables", type=str, nargs="+", help="Setup wearable integration (platforms)")
    parser.add_argument("--health-categories", type=str, nargs="+", default=["heart_rate", "steps", "sleep"], help="Health data categories")
    parser.add_argument("--health-sync", type=str, nargs="+", help="Setup health data sync (data types)")
    parser.add_argument("--sync-strategy", type=str, default="bidirectional", help="Sync strategy")
    parser.add_argument("--mcp-ai", type=str, nargs="+", help="Setup MCP/AI integration (providers)")
    parser.add_argument("--ai-features", type=str, nargs="+", default=["chat", "health_insights"], help="AI features to enable")
    parser.add_argument("--store-compliance", type=str, choices=["ios", "android", "both"], help="Check store compliance")
    parser.add_argument("--app-type", type=str, default="health", help="App type for compliance check")
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

    if args.figma:
        result = await agent.setup_figma_integration(args.figma, args.token_format)
        print(result.output)
        return

    if args.wearables:
        result = await agent.setup_wearable_integration(args.wearables, args.health_categories)
        print(result.output)
        return

    if args.health_sync:
        result = await agent.setup_health_data_sync(args.health_sync, args.sync_strategy)
        print(result.output)
        return

    if args.mcp_ai:
        result = await agent.setup_mcp_ai_integration(args.mcp_ai, args.ai_features)
        print(result.output)
        return

    if args.store_compliance:
        result = await agent.check_store_compliance(args.store_compliance, args.app_type)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Sophie - Mobile Developer")
    print("=========================")
    print("Specialties: React Native, PWA, Wearables, Figma, MCP/AI, Store Compliance")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
