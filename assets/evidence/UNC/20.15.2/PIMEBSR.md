# 查询EBSR信息（DSP PIMEBSR）

- [命令功能](#ZH-CN_CONCEPT_0000001550121218__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550121218__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550121218__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550121218__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550121218__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001550121218__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550121218)

该命令用于显示EBSR信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001550121218)

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550121218)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550121218)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| BSRADDR | 当选ASBSR地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为可选参数。<br>参数含义：该参数用来表示当选ASBSR地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| MASTERSLAVETYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |

#### [使用实例](#ZH-CN_CONCEPT_0000001550121218)

显示EBSR信息：

```
DSP PIMEBSR:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0  操作成功。

结果如下
--------
                 VPN实例名称  =  _public_
                      地址族  =  IPv4单播
               当选ASBSR地址  =  192.168.1.1
    该BSR是否为管理域中的BSR  =  管理区域BSR
                      组地址  =  239.0.0.1
              组地址掩码长度  =  16
             当选ASBSR优先级  =  0
           当选ASBSR哈希长度  =  30
               当选ASBSR状态  =  Elected状态
      当选ASBSR成为BSR的时间  =  00:17:12
当选ASBSR发送下一个BSM的时间  =  00:00:12
                候选RP的个数  =  1
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001550121218)

| 输出项名称 | 输出项解释 |
| --- | --- |
| VPN实例名称 | 用来表示VPN实例名称。 |
| 地址族 | 用于表示地址族类型。 |
| 当选ASBSR地址 | 用来表示当选ASBSR地址。 |
| 该BSR是否为管理域中的BSR | 用来表示该BSR是否为管理域中的BSR，包括：<br>- 未配置表示没有配置CBSR区域。<br>- Global域表示路由器为Global域中的CBSR。<br>- 管理区域BSR表示PIM-SM域中划分多个BSR管理区域，从而实现RP-Set分发机制。 |
| 组地址 | 用来表示组地址。 |
| 组地址掩码长度 | 用来表示组地址掩码长度。 |
| 当选ASBSR优先级 | 用来表示当选ASBSR优先级。 |
| 当选ASBSR哈希长度 | 用来表示当选ASBSR哈希长度。 |
| 当选ASBSR状态 | 用来表示当选ASBSR状态，包括：<br>- Accept Any状态表示该设备上没有配置CBSR，当已知的Elect BSR Down掉后，Elect BSR状态就会变为Accept Any状态。<br>- Accept Preferred状态表示该设备上没有配置CBSR，并且知道当前的Elected BSR。<br>- Candidate状态表示该设备配置了CBSR，但网络中已存在Elected BSR。<br>- Pending状态表示该设备配置了CBSR，网络中尚未选举出BSR。<br>- Elected状态表示该设备配置了CBSR，并且当选为BSR。<br>- Waiting to be Pending状态表示等待选举BSR。 |
| 当选ASBSR成为BSR的时间 | 用来表示当选ASBSR成为BSR的时间。 |
| 当选ASBSR发送下一个BSM的时间 | 用来表示当选ASBSR发送下一个BSM的时间。 |
| 候选RP的个数 | 用来表示候选RP的个数。 |
