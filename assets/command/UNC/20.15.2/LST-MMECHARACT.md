---
id: UNC@20.15.2@MMLCommand@LST MMECHARACT
type: MMLCommand
name: LST MMECHARACT（查询MME属性配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MMECHARACT
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-SGSN_S10_S16_S3接口管理
- MME属性
status: active
---

# LST MMECHARACT（查询MME属性配置信息）

## 功能

**适用网元：MME**

该命令用于查询对端MME的属性信息。

## 注意事项

- 该命令执行后立即生效。
- 当不输入查询条件时，显示所有记录信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 对端设备范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指示对端MME设备范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_MME（所有MME）”<br>- “SPECIAL_MME（指定MME）”<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对端MME的信令面IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPv4）”<br>- “IPV6（IPv6）”<br>默认值：无<br>配置原则：<br>- IPv4: 表示对端MME的信令面IP地址为IPv4类型。<br>- IPv6：表示对端MME的信令面IP地址为IPv6类型。 |
| IPV4 | MME IPv4信令面地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对端MME的信令面IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV4（IPv4）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.1~255.255.255.254<br>默认值：无<br>配置原则：有效的IPv4地址必须是A、B或者C类地址，且不能为环回地址（127.x.y.z）。 |
| MASKV4 | IPv4掩码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对端MME的信令面IPv4地址的掩码。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV4（IPv4）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.1~255.255.255.255<br>默认值：无<br>说明：- 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| IPV6 | MME IPv6信令面地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对端MME的信令面IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV6（IPv6）”<br>后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8） |
| MASKV6 | IPv6子网前缀长度 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定子网前缀的长度。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV6（IPv6）”<br>后生效。<br>数据来源：全网规划<br>取值范围：1~128<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MMECHARACT]] · MME属性配置信息（MMECHARACT）

## 使用实例

不输入查询条件，查询表中全部MME的属性信息：

LST MMECHARACT:;

```
%%LST MMECHARACT:;%%
RETCODE = 0  操作成功。

所有MME查询结果如下
-------------------------
                               对端设备范围  =  所有MME
                            是否携带PRA信元  =  否
                   是否携带无线寻呼能力信元  =  否
                           CIoT优化支持指示  =  NULL
                   是否携带扩展接入限制数据  =  否
                     是否携带UE附加安全能力  =  否
                     NB-IoT状态上报订阅信息  =  否
                 是否携带MME Identifier信元  =  否
                           是否携带RAT Type  =  否
是否携带Secondary RAT Usage Data Report信元  =  否
                           是否限制最大速率  =  否
                是否携带SGW S11-U FTEID信元  =  否
                      是否携带UE NR安全能力  =  否
                    SGW/PGW地址信元携带策略  =  透传
                       是否携带扩展跟踪信息  =  否
                       是否传递PCRF签约RFSP  =  否
                         是否传递PCRF签约NI  =  否
                                       描述  =  NULL
仍有后续报告输出
---   END

%%LST MMECHARACT:;%%
RETCODE = 0  操作成功。

指定MME IPv4查询结果如下
--------------------
                               对端设备范围  =  指定MME
                                 IP地址类型  =  IPv4
                         MME IPv4信令面地址  =  192.168.168.12
                                   IPv4掩码  =  255.255.255.0
                            是否携带PRA信元  =  否
                   是否携带无线寻呼能力信元  =  否
                           CIoT优化支持指示  =  NULL
                   是否携带扩展接入限制数据  =  否
                     是否携带UE附加安全能力  =  否
                     NB-IoT状态上报订阅信息  =  否
                 是否携带MME Identifier信元  =  否
                           是否携带RAT Type  =  否
是否携带Secondary RAT Usage Data Report信元  =  否
                           是否限制最大速率  =  否
                是否携带SGW S11-U FTEID信元  =  否
                      是否携带UE NR安全能力  =  否
                    SGW/PGW地址信元携带策略  =  透传
                       是否携带扩展跟踪信息  =  否
                       是否传递PCRF签约RFSP  =  否
                         是否传递PCRF签约NI  =  否
                                       描述  =  NULL
(结果个数 = 2)
共2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MMECHARACT.md`
