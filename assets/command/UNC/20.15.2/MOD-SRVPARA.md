---
id: UNC@20.15.2@MMLCommand@MOD SRVPARA
type: MMLCommand
name: MOD SRVPARA（修改业务参数配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SRVPARA
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
max_records: 32
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 业务参数管理
status: active
---

# MOD SRVPARA（修改业务参数配置）

## 功能

![](修改业务参数配置（MOD SRVPARA）_51174334.assets/notice_3.0-zh-cn_2.png)

如果业务参数类型选择PASSIVE模式参数，此操作会重启FTP服务，导致计费中心客户端会中断1~2秒。

**适用NF：NCG**

用于修改NCG相关参数。

执行命令之前，可执行 [**LST SRVPARA**](查询业务参数配置（LST SRVPARA）_51174335.md) 命令查询当前配置的参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为32。
- 起始端口与结束端口中间不能包含20048、2049、32769、2020端口。
- 该命令存在系统初始设置记录，参数的初始设置值如下表：

| SRVPARATYPE | GATRACEMSGLEN | STARTPORT | ENDPORT | SRVPARAVALUE | CLIENTALIVECOUNTMAX | CLIENTALIVEINTERVAL | SFTPMAXCPULIMIT | FTPMAXCPULIMIT | GALICVOLALMPCT | GALICVOLALMRST | GALICALMDEPRD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GATRACEMSGPARA | SHORT | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL |
| PASSIVEPARA | NULL | 20050 | 20100 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL |
| ANOTHERNODEDOWNPARA | NULL | NULL | NULL | OFF | NULL | NULL | NULL | NULL | NULL | NULL | NULL |
| CDMPULLMODEPARA | NULL | NULL | NULL | NULL | 0 | 300 | 100 | 100 | NULL | NULL | NULL |
| GALICCTRLALM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 80 | 70 | 20 |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVPARATYPE | 业务参数类型 | 可选必选说明：必选参数<br>参数含义：用于指定对哪一类业务参数进行修改。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GATRACEMSGPARA：Ga跟踪消息长度。<br>- PASSIVEPARA：PASSIVE模式参数。<br>- ANOTHERNODEDOWNPARA：另一节点发生故障。<br>- CDMPULLMODEPARA：PULL分发模式参数。<br>- GALICCTRLALM：GA License控制告警阈值。<br>默认值：无<br>配置原则：如果使用ANOTHERNODEDOWNPARA功能，请确保配置监控任务或者上报ALM-82000长时间未取话单告警之前，开启SRVPARAVALUE开关。 |
| GATRACEMSGLEN | Ga跟踪消息长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVPARATYPE”配置为“GATRACEMSGPARA”时为条件可选参数。<br>参数含义：用于设置Ga跟踪消息并且消息类型是DataTransferRequest时的上报长度控制。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SHORT：Ga跟踪消息，且消息类型为DataTransferRequest时候，只上报24个字节的GTP’消息。<br>- LONG：Ga跟踪消息，且消息类型为DataTransferRequest时候，上报完整的GTP’报文。<br>默认值：无<br>配置原则：无 |
| STARTPORT | 起始端口 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVPARATYPE”配置为“PASSIVEPARA”时为条件可选参数。<br>参数含义：PULL模式下FTP PASSIVE和PORT模式的起始端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1024～65535。<br>默认值：无<br>配置原则：起始端口必须小于结束端口。 |
| ENDPORT | 结束端口 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVPARATYPE”配置为“PASSIVEPARA”时为条件可选参数。<br>参数含义：PULL模式下FTP PASSIVE和PORT模式的结束端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1024～65535。<br>默认值：无<br>配置原则：结束端口必须大于起始端口。 |
| SRVPARAVALUE | 业务控制参数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVPARATYPE”配置为“ANOTHERNODEDOWNPARA”时为条件可选参数。<br>参数含义：软参值的开关状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：无 |
| CLIENTALIVECOUNTMAX | SFTP最大超时次数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVPARATYPE”配置为“CDMPULLMODEPARA”时为条件可选参数。<br>参数含义：PULL模式下SFTP服务端的ClientAliveCountMax参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：0<br>配置原则：无 |
| CLIENTALIVEINTERVAL | SFTP服务器端向客户端请求消息的时间间隔 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVPARATYPE”配置为“CDMPULLMODEPARA”时为条件可选参数。<br>参数含义：PULL模式下SFTP服务端的ClientAliveInterval参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～86400。<br>默认值：300<br>配置原则：无 |
| SFTPMAXCPULIMIT | SFTP CPU最高占比（%） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVPARATYPE”配置为“CDMPULLMODEPARA”时为条件可选参数。<br>参数含义：PULL模式下SFTP服务端的CPU最高占比。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～100。<br>默认值：100<br>配置原则：无 |
| FTPMAXCPULIMIT | FTP CPU最高占比（%） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVPARATYPE”配置为“CDMPULLMODEPARA”时为条件可选参数。<br>参数含义：PULL模式下FTP服务端的CPU最高占比。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～100。<br>默认值：100<br>配置原则：无 |
| GALICVOLALMPCT | 容量告警百分比（%） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVPARATYPE”配置为“GALICCTRLALM”时为条件可选参数。<br>参数含义：该参数用于指定容量告警百分比。当系统中已使用的资源控制项数目在“持续时间”内的平均值与License允许的数目比值大于该参数设定的值时，系统将产生<br>[ALM-82015](../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82015 License过载_51174210.md)<br>告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为80～99。<br>默认值：80<br>配置原则：容量告警百分比必须大于容量告警恢复百分比。 |
| GALICVOLALMRST | 容量告警恢复百分比（%） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVPARATYPE”配置为“GALICCTRLALM”时为条件可选参数。<br>参数含义：该参数用于指定容量告警恢复百分比。系统已经产生该资源控制项的容量告警后，当已使用的资源控制项数目在“持续时间”内的平均值与License允许的数目比值小于该参数设定的值时，系统将恢复<br>[ALM-82015](../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82015 License过载_51174210.md)<br>告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～99。<br>默认值：70<br>配置原则：容量告警百分比必须大于容量告警恢复百分比。 |
| GALICALMDEPRD | 告警检测周期（分钟） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SRVPARATYPE”配置为“GALICCTRLALM”时为条件可选参数。<br>参数含义：告警<br>[ALM-82015](../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/NCG/ALM-82015 License过载_51174210.md)<br>的检测周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～480。<br>默认值：20<br>配置原则：无 |

## 操作的配置对象

- [业务参数配置（SRVPARA）](configobject/UNC/20.15.2/SRVPARA.md)

## 使用实例

- 业务参数类型设置为“Ga跟踪消息长度”，Ga跟踪消息长度设置为“LONG”：
  ```
  MOD SRVPARA: SRVPARATYPE=GATRACEMSGPARA, GATRACEMSGLEN=LONG;
  ```
- 业务参数类型设置为“PASSIVE模式参数”，起始端口设置为20060，结束端口设置为20090：
  ```
  MOD SRVPARA: SRVPARATYPE=PASSIVEPARA, STARTPORT=20060, ENDPORT=20090;
  ```
-
  业务参数类型设置为“另一节点发生故障”，软参值的开关状态设置为“开启”：

  ```
  MOD SRVPARA: SRVPARATYPE=ANOTHERNODEDOWNPARA, SRVPARAVALUE=ON;
  ```
- 业务参数类型设置为“PULL分发模式参数”，SFTP最大超时次数设置为5，SFTP服务器端向客户端请求消息的时间间隔设置为60，SFTP CPU最高占比（%）设置为90，FTP CPU最高占比（%）设置为90：
  ```
  MOD SRVPARA: SRVPARATYPE=CDMPULLMODEPARA, CLIENTALIVECOUNTMAX=5, CLIENTALIVEINTERVAL=60, SFTPMAXCPULIMIT=90, FTPMAXCPULIMIT=90;
  ```
- 业务参数类型设置为“GA License控制告警阈值”，容量告警百分比设置为85，容量告警恢复百分比设置为75，告警检测周期设置为30：
  ```
  MOD SRVPARA: SRVPARATYPE=GALICCTRLALM, GALICVOLALMPCT=85, GALICVOLALMRST=75, GALICALMDEPRD=30;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改业务参数配置（MOD-SRVPARA）_51174334.md`
