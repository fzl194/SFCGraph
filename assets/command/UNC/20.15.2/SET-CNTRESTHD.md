---
id: UNC@20.15.2@MMLCommand@SET CNTRESTHD
type: MMLCommand
name: SET CNTRESTHD（设置容器资源阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CNTRESTHD
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 容器管理
status: active
---

# SET CNTRESTHD（设置容器资源阈值）

## 功能

![](设置容器资源阈值（SET CNTRESTHD）_61025381.assets/notice_3.0-zh-cn_2.png)

告警阈值的调整会影响告警的触发条件，请注意设置合理的告警阈值。

该命令用于设置容器的资源告警上报、清除阈值，CPU突变检测阈值和检测间隔，容器网络亚健康资源检测。

## 注意事项

- 告警阈值会持久化写入到Gauss数据库中，各容器阈值更新会有一定的延迟，可通过[**DSP CNTRESSTAT**](查询容器资源信息（DSP CNTRESSTAT）_60785913.md)命令查看。
- 本命令若按照“容器类型”配置后再次按照“网元级”配置，则不覆盖该网元下的“容器类型”的配置。

- 该命令系统初始值参数设置如下：

| 参数名称 | 初始值 |
| --- | --- |
| 网络亚健康告警开关 | on |
| 单链路丢包率阈值(%) | 2.0 |
| 网络亚健康告警上报阈值(%) | 70 |
| 网络亚健康告警清除阈值(%) | 30 |
| 网络亚健康响应阈值(ms) | 200 |

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SETCNTTHD_RES_NAME | 资源名称 | 可选必选说明：必选参数。<br>参数含义：用于指示系统当前设置的资源名称。<br>取值范围：<br>- cpu(CPU)<br>- memory(内存)<br>- net(网络)<br>- disk(磁盘)<br>默认值：无。<br>配置原则：无。 |
| SETCNTTHD_RES_CPU | CPU阈值类型 | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“cpu(CPU)”<br>时为必选参数。<br>参数含义：用于指示系统当前设置的CPU阈值类型。<br>取值范围：<br>- cpu_usage(cpu告警阈值)<br>- cpu_change(cpu突变阈值)<br>默认值：无。<br>配置原则：无。 |
| SETCNTTHD_RES_DISK | DISK阈值类型 | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“disk(磁盘)”<br>时为必选参数。<br>参数含义：用于指示系统当前设置的disk阈值类型。<br>取值范围：<br>- disk_usage(disk告警阈值)<br>- inode_usage(inode告警阈值)<br>默认值：无。<br>配置原则：无。 |
| SETCNTTHD_MEID | 网元ID | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“memory(内存)”<br>时为必选参数，在<br>**“CPU阈值类型”**<br>取值为<br>“cpu_usage(cpu告警阈值)”<br>时为必选参数；或在<br>“资源名称”<br>取值为<br>“disk(磁盘)”<br>且在<br>“DISK阈值类型”<br>取值为<br>“disk_usage(disk告警阈值)”<br>或<br>“inode_usage(inode告警阈值)”<br>时为必选参数。<br>参数含义：当前需要设置告警阈值的网元ID，即应用ID。<br>取值范围：整数类型，取值范围0~65535。<br>默认值：无。<br>配置原则：无。 |
| SETCNTTHD_GENERATE_SWITCH | 开关 | 可选必选说明：该参数在<br>**“CPU阈值类型”**<br>取值为<br>“cpu_change(cpu突变阈值)”<br>时为必选参数。<br>参数含义：CPU突变检测是否开启。<br>取值范围：<br>- on(ON)<br>- off(OFF)<br>默认值：无。<br>配置原则：无。 |
| SETCNTTHD_GENERATE_TH | 阈值(%) | 可选必选说明：该参数在<br>**“开关”**<br>取值为<br>“on(ON)”<br>时为必选参数。<br>参数含义：当前需要设置的CPU检测阈值，单位为百分比。<br>取值范围：整数类型，取值范围3~100。<br>默认值：无。<br>配置原则：无。 |
| SETCNTTHD_GENERATE_INTERVAL | CPU突变检测间隔(s) | 可选必选说明：该参数在<br>**“开关”**<br>取值为<br>“on(ON)”<br>时为必选参数。<br>参数含义：当前需要设置的CPU突变检测时间间隔，单位为秒。<br>取值范围：整数类型，取值范围3~60。<br>默认值：无。<br>配置原则：无。 |
| SETCNTTHD_ALARM_GENERATE_TH | 告警上报阈值(%) | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“memory(内存)”<br>时为必选参数，在<br>“资源名称”<br>取值为<br>“cpu(CPU)”<br>且在"<br>**CPU阈值类型**<br>"取值为"cpu_usage(cpu告警阈值)"时为必选参数；或在<br>“资源名称”<br>取值为<br>“disk(磁盘)”<br>且在<br>“DISK阈值类型”<br>取值为<br>“disk_usage(disk告警阈值)”<br>或<br>“inode_usage(inode告警阈值)”<br>时为必选参数。<br>参数含义：用于指示系统当前设置的告警上报阈值。<br>取值范围：整数类型，取值范围 2~100。<br>默认值： 无。<br>配置原则：告警上报阈值应大于告警清除阈值。 |
| SETCNTTHD_ALARM_CLEAR_TH | 告警清除阈值(%) | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“memory(内存)”<br>时为必选参数，在<br>“资源名称”<br>取值为<br>“cpu(CPU)”<br>且在"<br>**CPU阈值类型**<br>"取值为"cpu_usage(cpu告警阈值)"时为必选参数；或在<br>“资源名称”<br>取值为<br>“disk(磁盘)”<br>且在<br>“DISK阈值类型”<br>取值为<br>“disk_usage(disk告警阈值)”<br>或<br>“inode_usage(inode告警阈值)”<br>时为必选参数。<br>参数含义：用于指示系统当前设置的告警清除阈值。<br>取值范围：整数类型，取值范围 1~99。<br>默认值： 无。<br>配置原则：告警清除阈值应小于告警上报阈值。 |
| SETCNTTHD_ALARM_TYPE | 阈值设置类型 | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“memory(内存)”<br>时为必选参数，在<br>“资源名称”<br>取值为<br>“cpu(CPU)”<br>且在"<br>**CPU阈值类型**<br>"取值为"cpu_usage(cpu告警阈值)"时为必选参数；或在<br>“资源名称”<br>取值为<br>“disk(磁盘)”<br>且在<br>“DISK阈值类型”<br>取值为<br>“disk_usage(disk告警阈值)”<br>或<br>“inode_usage(inode告警阈值)”<br>时为必选参数。<br>参数含义：用于指示系统当前设置的阈值类型。<br>取值范围：<br>- byME(网元级)<br>- byContainerType(容器类型)<br>默认值：无。<br>配置原则：无。 |
| SETCNTTHD_CNT_TYPE | 容器类型 | 可选必选说明：该参数在<br>“阈值设置类型”<br>取值为<br>“byContainerType(容器类型)”<br>时为必选参数。<br>参数含义：用于指示系统按照容器类型设置告警阈值。<br>取值范围：字符串类型，字符串长度范围为2~256个字符。<br>默认值：无。<br>配置原则：通过<br>[**DSP CNTINFO**](查询容器部署信息（DSP CNTINFO）_60666141.md)<br>命令查询容器类型。 |
| SETCNTTHD_NETSUBHEALTH | 网络亚健康资源检测 | 可选必选说明：该参数在<br>“资源名称”<br>取值为<br>“net(网络)”<br>时为必选参数。<br>参数含义：用于指示当前设置的网络亚健康类型。<br>取值范围：<br>- netsubhealth(网络亚健康)。<br>默认值：无。<br>配置原则：无。 |
| SETCNTTHD_GENERATE_NET_SWITCH | 网络亚健康告警开关 | 可选必选说明：该参数在<br>**“网络亚健康资源检测”**<br>取值为<br>“netsubhealth(网络亚健康)”<br>时为必选参数。<br>参数含义：用于指示网络亚健康告警是否上报。<br>取值范围：<br>- on(ON)<br>- off(OFF)<br>默认值：无。<br>配置原则：无。 |
| SETCNTTHD_PACKET_LOST_NET_TH | 单链路丢包率阈值(%) | 可选必选说明：该参数在<br>**“网络亚健康告警开关”**<br>取值为<br>“on(ON)”<br>时为必选参数。<br>参数含义：用于指示每条链路的丢包阈值。<br>取值范围：字符串类型，取值范围 0~99<br>默认值：无。<br>配置原则：无。 |
| SETCNTTHD_ALARM_GENERATE_NET_TH | 网络亚健康告警上报阈值(%) | 可选必选说明：该参数在<br>**“网络亚健康告警开关”**<br>取值为<br>“on(ON)”<br>时为必选参数。<br>参数含义：用于指示网络亚健康告警上报的阈值。<br>取值范围：整数类型，取值范围 1~100。<br>默认值：无。<br>配置原则：告警清除阈值应小于告警上报阈值。 |
| SETCNTTHD_ALARM_CLEAR_NET_TH | 网络亚健康告警清除阈值(%) | 可选必选说明：该参数在<br>**“网络亚健康告警开关”**<br>取值为<br>“on(ON)”<br>时为必选参数。<br>参数含义：用于指示网络亚健康告警清除的阈值。<br>取值范围：整数类型，取值范围 0~99。<br>默认值：无。<br>配置原则：告警清除阈值应小于告警上报阈值。 |
| SETCNTTHD_NETSUBHEALTH_RESP_TH | 网络亚健康响应阈值(ms) | 可选必选说明：该参数在<br>**“网络亚健康告警开关”**<br>取值为<br>“on(ON)”<br>时为必选参数。<br>参数含义：用于指示网络亚健康响应的阈值。<br>取值范围：整数类型，取值范围 5~20000。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CNTRESTHD]] · 容器资源阈值（CNTRESTHD）

## 使用实例

1. 按照网元设置容器告警上报、清除阈值。
  ```
  %%SET CNTRESTHD: SETCNTTHD_RES_NAME=memory, SETCNTTHD_MEID=0, SETCNTTHD_ALARM_GENERATE_TH=80, SETCNTTHD_ALARM_CLEAR_TH=65, SETCNTTHD_ALARM_TYPE=byME;%% 
  RETCODE = 0  操作成功    
  操作结果  =  SUCCESS 
  (结果个数 = 1)  
  ---    END
  ```

2. 按照容器类型设置容器告警上报、清除阈值。
  ```
  %%SET CNTRESTHD: SETCNTTHD_RES_NAME=memory, SETCNTTHD_MEID=0, SETCNTTHD_ALARM_GENERATE_TH=80, SETCNTTHD_ALARM_CLEAR_TH=65, SETCNTTHD_ALARM_TYPE=byContainerType, SETCNTTHD_CNT_TYPE="cspopsagent-software";%% 
  RETCODE = 0  执行成功    
  操作结果  =  SUCCESS 
  (结果个数 = 1)  
  ---    END 
  ```

3. 设置CPU检测阈值。
  ```
  %%SET CNTRESTHD: SETCNTTHD_RES_NAME=cpu, SETCNTTHD_RES_CPU=cpu_change, SETCNTTHD_GENERATE_SWITCH=on, SETCNTTHD_GENERATE_TH=60, SETCNTTHD_GENERATE_INTERVAL=18;%% 
  RETCODE = 0  操作成功    
  操作结果  =  SUCCESS 
  (结果个数 = 1)  
  ---    END
  ```

4. 设置容器网络检测阈值。
  ```
  %%SET CNTRESTHD: SETCNTTHD_RES_NAME=net, SETCNTTHD_NETSUBHEALTH=netsubhealth, SETCNTTHD_GENERATE_NET_SWITCH=on, SETCNTTHD_PACKET_LOST_NET_TH="1.0", SETCNTTHD_ALARM_GENERATE_NET_TH=19, SETCNTTHD_ALARM_CLEAR_NET_TH=9, SETCNTTHD_NETSUBHEALTH_RESP_TH=333;%%
  RETCODE = 0  操作成功
  操作结果  =  SUCCESS
  (结果个数 = 1)
  ---    END
  ```

5. 按网元ID设置磁盘分区使用量disk_usage上报告警和清除告警的阈值
  ```
  %%SET CNTRESTHD: SETCNTTHD_RES_NAME=disk, SETCNTTHD_RES_DISK=disk_usage, SETCNTTHD_MEID=0, SETCNTTHD_ALARM_GENERATE_TH=90, SETCNTTHD_ALARM_CLEAR_TH=85, SETCNTTHD_ALARM_TYPE=byME;%% 
  RETCODE = 0  操作成功    
  操作结果  =  SUCCESS 
  (结果个数 = 1)  
  ---    END
  ```
6. 按容器类型设置磁盘inode的使用量inode_usage上报告警和清除告警的阈值
  ```
  %%SET CNTRESTHD: SETCNTTHD_RES_NAME=disk, SETCNTTHD_RES_DISK=inode_usage, SETCNTTHD_MEID=0, SETCNTTHD_ALARM_GENERATE_TH=90, SETCNTTHD_ALARM_CLEAR_TH=85, SETCNTTHD_ALARM_TYPE=byContainerType, SETCNTTHD_CNT_TYPE="fileserver-software";%% 
  RETCODE = 0  操作成功    
  操作结果  =  SUCCESS 
  (结果个数 = 1)  
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CNTRESTHD.md`
