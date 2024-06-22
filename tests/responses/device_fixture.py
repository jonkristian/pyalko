"""
Generated by generator/generator.py - 2024-06-22 16:23:41.214380
"""
import pytest


@pytest.fixture()
def device_fixture_response():
    return {'thingName': 'string', 'thingType': 'string', 'thingAttributes': {'thingName': 'string', 'thingType': 'string', 'articleNumber': 'string', 'serialNumber': 'string', 'firmwareWifi': 'string', 'hardwareVersionWifi': 'string', 'firmwareMain': 'string', 'firmwareMainLocalization': 'string', 'serialNumberMain': 'string', 'hardwareVersionMain': 'string', 'thingModel': 'string', 'firmwareWifiDriver': 'string', 'serialNumberWifi': 'string', 'fotaMode': 'string', 'betatester': 'string'}, 'accessInformation': {'accessId': 'string', 'thingName': 'string', 'userId': 'string', 'idpAccountId': 'string', 'userEmail': 'string', 'accessAlias': 'string', 'accessAdmin': 'boolean', 'accessCreated': 'string'}, 'accesses': [{'accessId': 'string', 'thingName': 'string', 'userId': 'string', 'idpAccountId': 'string', 'userEmail': 'string', 'accessAlias': 'string', 'accessAdmin': 'boolean', 'accessCreated': 'string'}], 'thingState': {'state': {'desired': {}, 'reported': {'isConnected': 'boolean', 'rssi': 'integer', 'batteryLevel': 'integer', 'operationState': 'string', 'operationSubState': 'string', 'operationSituation': 'string', 'operationError': {'code': 'integer', 'type': 'string', 'description': 'string'}, 'nextOperation': 'integer', 'remainingDuration': 'integer', 'operationTimeTotal': 'integer', 'operationTimeMowing': 'integer', 'operationTimeWheelMotorLeft': 'integer', 'operationTimeWheelMotorRight': 'integer', 'operationTimeBlade': 'integer', 'mowingCycles': 'integer', 'chargingCycles': 'integer', 'remainingBladeLifetime': 'integer', 'rtc': 'string', 'languageSettings': {'selected': 'string', 'supported': ['string']}, 'chargingCurrent': 'integer', 'tiltSlope': 'integer', 'entryPoints': ['integer'], 'rainSensor': 'boolean', 'rainDelay': 'integer', 'ecoMode': 'boolean', 'boundaryOverlap': 'integer', 'mowingWindows': {'monday': {'window_1': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}, 'window_2': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}}, 'tuesday': {'window_1': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}, 'window_2': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}}, 'wednesday': {'window_1': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}, 'window_2': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}}, 'thursday': {'window_1': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}, 'window_2': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}}, 'friday': {'window_1': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}, 'window_2': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}}, 'saturday': {'window_1': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}, 'window_2': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}}, 'sunday': {'window_1': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}, 'window_2': {'activityMode': 'boolean', 'marginMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer', 'narrowPassageMode': 'boolean'}}}, 'situationFlags': {'operationPermitted': 'boolean', 'batteryWeak': 'boolean', 'batteryFailure': 'boolean', 'batteryWeakSticky': 'boolean', 'mowingWindow': 'boolean', 'marginMowingCompleted': 'boolean', 'userInteraction': 'boolean', 'loopSignalValid': 'boolean', 'chargerContact': 'boolean', 'chargerActive': 'boolean', 'chargerAllowsRestart': 'boolean', 'chargerFailure': 'boolean', 'manualOperation': 'boolean', 'robotIsActive': 'boolean', 'issueDisplay': 'boolean', 'homingTriggerSchedule': 'boolean', 'homingTriggerBatteryWaek': 'boolean', 'homingTriggerUserRequest': 'boolean', 'homingTriggerRain': 'boolean', 'homingTriggerTemperature': 'boolean', 'homingTriggerMowingUnitOverload': 'boolean', 'homingTriggerRestart': 'boolean', 'dayCancelled': 'boolean', 'rainDetected': 'boolean', 'rainAllowsMowing': 'boolean', 'temperatureMonitoringActive': 'boolean', 'temperatureAllowsMowing': 'boolean', 'temperatureAllowsHoming': 'boolean', 'temperatureAllowsCharging': 'boolean', 'wheelMotorTemperatureHigh': 'boolean', 'stopAfterIssue': 'boolean', 'bladeService': 'boolean', 'homingTriggerFrost': 'boolean', 'frostDetected': 'boolean', 'frostAllowsMowing': 'boolean', 'smarthomeActive': 'boolean'}, 'remainingDurationPercentage': 'integer', 'operationIssue': {'code': 'integer', 'class': 'integer', 'data': 'integer', 'flag': 'integer'}, 'rainSensitivity': 'integer', 'frostSensor': 'boolean', 'frostDelay': 'integer', 'frostThreshold': 'integer', 'calibration': {'loop': {'slope': {'l': 'integer', 'r': 'integer'}, 'peak': {'l': 'integer', 'r': 'integer'}, 'length': 'integer'}, 'acc': {'offset': {'x': 'integer', 'y': 'integer'}, 'security': {'stopAngel': 'integer', 'orientation': 'integer', 'stopAngle': 'integer'}}, 'hall': {'zero': 'integer', 'trigger': 'integer', 'neutral': {'x': 'integer', 'y': 'integer'}, 'triggerLevel': 'integer', 'flag': 'integer'}, 'qhk': {'flag': 'boolean', 'left': 'integer', 'right': 'integer', 'peak': 'integer', 'upperBound': 'integer', 'lowerBound': 'integer'}}, 'batteryWeakVoltage': 'integer', 'bladesService': 'integer', 'sideBumpTrigger': 'integer', 'restartLevel': 'integer', 'latSlopeCompUp': 'integer', 'latSlopeCompDown': 'integer', 'longDistanceTurn': 'integer', 'mowingStrategy': 'boolean', 'demoMode': 'boolean', 'marginMowing': 'boolean', 'bladeSpeed': 'integer', 'battery': {'chargingCurrent': 'integer', 'voltage': 'integer'}, 'loop': {'insideField': {'left': 'string', 'right': 'string'}, 'signalStrength': {'left': 'integer', 'right': 'integer'}, 'value': {'left': 'integer', 'right': 'integer'}, 'calibrationValue': {'left': 'integer', 'right': 'integer'}}, 'acceleration': {'x': 'integer', 'y': 'integer', 'z': 'integer'}, 'hall': {'bumper': 'string', 'x': 'integer', 'y': 'integer', 'bumperTriggered': 'boolean', 'z': 'string', 'value1': 'integer', 'value2': 'integer', 'value3': 'integer', 'value4': 'integer', 'value5': 'integer'}, 'temperature': {'battery': 'integer', 'motor': 'integer', 'environment': 'integer'}, 'rpm': {'set': 'integer', 'current': 'integer'}, 'motorCurrent': {'mowingUnit': 'integer', 'wheel': {'left': 'integer', 'right': 'integer'}}, 'manualMarginMowing': 'boolean', 'offPitch': 'boolean', 'resetBladesService': 'boolean', 'qhk': {'flag': 'boolean', 'angle': 'integer'}, 'manualMowing': {'activityMode': 'boolean', 'marginMode': 'boolean', 'narrowPassageMode': 'boolean', 'startHour': 'integer', 'startMinute': 'integer', 'duration': 'integer', 'entryPoint': 'integer'}, 'ipaddress': 'string'}, 'delta': {}}}, 'pim': {'artnumber': 'string', 'accessoryList': [{'id': 'integer', 'artnumber': 'integer'}], 'price': 'integer', 'brand': [{'id': 'integer', 'name': 'string'}], 'additionalDocuments': [{'doctype': 'string', 'docid': 'string', 'docstorecat': 'string', 'docname': 'string', 'docnumber': 'string', 'version': 'string'}], 'title': 'string', 'productHierarchy': 'string', 'crosssellingList': [{'id': 'string', 'artnumber': 'string'}], 'attributeList': [{'id': 'string', 'key': 'string', 'name': 'string', 'attrtype': 'string', 'internalValue': 'string', 'label': 'string', 'value_from': 'integer', 'value_to': 'integer', 'unit': 'string', 'value_once': 'string', 'parent': {'id': 'string', 'name': 'string', 'exportToShop': 'boolean', 'exportToChannable': 'boolean', 'label': 'string'}, 'showShop': 'boolean', 'showDatasheet': 'boolean', 'group': [{'id': 'string', 'name': 'string', 'label': 'string'}]}], 'appimages': [{'image': {'update': 'integer', 'mimetype': 'string', 'filename': 'string', 'fullpath': 'string'}}], 'images': []}}
