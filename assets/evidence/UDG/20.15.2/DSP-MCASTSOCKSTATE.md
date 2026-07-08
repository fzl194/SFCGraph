# 查询组播Socket信息（DSP MCASTSOCKSTATE）

- [命令功能](#ZH-CN_CONCEPT_0000001600840577__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600840577__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600840577__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600840577__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600840577__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600840577__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600840577)

该命令用于显示组播Socket信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600840577)

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600840577)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600840577)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| COMPONENTNAME | 组件名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组件名称。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PIMCORE：PIMCORE组件。<br>- DGMP：DGMP组件。<br>- PIMBSR：PIMBSR组件。<br>- PIMAGENT：PIMAGENT组件。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| IFNAME | 接口名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“COMPONENTNAME”配置为“DGMP”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“COMPONENTNAME”配置为“PIMAGENT”时为可选参数。<br>参数含义：该参数用于表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600840577)

查询组播Socket信息：

```
DSP MCASTSOCKSTATE:VRFNAME= "_public_",ADDRESSFAMILY=ipv4unicast,COMPONENTNAME=PIMCORE;
```

```
RETCODE = 0  操作成功。

结果如下
--------
  VPN实例名称  =  _public_
       地址族  =  IPv4单播
     组件名称  =  Pimcore组件
      组件PID  =  14549016
      组件CID  =  2162032664
   Socket状态  =  Established
Socket组件CID  =  0x80650080
   Socket索引  =  1
       管道ID  =  524314
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600840577)

| 输出项名称 | 输出项解释 |
| --- | --- |
| VPN实例名称 | 用于表示VPN实例名称。 |
| 地址族 | 用于表示地址族类型。 |
| 组件名称 | 用于表示组件名称。 |
| 组件PID | 用于表示组件PID。 |
| 组件CID | 用于表示组件CID。 |
| Socket状态 | 用于表示Socket状态，包括：<br>- Noinfo表示无状态。<br>- Wait Register表示等待注册。<br>- To create表示正在创建。<br>- To establish表示正在建立。<br>- Established表示已建立。<br>- Close socket表示关闭Socket。<br>- Close pipe表示关闭管道。<br>- To noinfo表示正在清除状态。<br>- Re create表示重试创建。<br>- Wait attach表示等待建连。<br>- Wait close attach表示等待停止建连。<br>- Wait deattach表示等待断连。<br>- Recreate Wait deattach表示重试等待断连。<br>- Wait close slave表示等待关闭备组件。<br>- Unknow表示未知状态。 |
| Socket组件CID | 用于表示Socket组件CID。 |
| Socket索引 | 用于表示Socket索引。 |
| 管道ID | 用于表示管道ID。 |
