---
id: UNC@20.15.2@MMLCommand@TST SDUPPATH
type: MMLCommand
name: TST SDUPPATH（测试SDUP路径）
nf: UNC
version: 20.15.2
verb: TST
object_keyword: SDUPPATH
command_category: 调测类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- Sdup接口管理
- Sdup接口调测
status: active
---

# TST SDUPPATH（测试SDUP路径）

## 功能

**适用网元：MME**

该命令用于通过发送Echo消息的方法测试本端与对端MME之间的SDUP路径是否正常。无论路径正常与否，都返回报文显示路径地址信息及路径状态；

## 注意事项

- 该命令执行后立即生效。
- 该命令执行过程中会产生一条临时的维护路径，执行结束后删除该维护路径。该命令只探测路径是否正常，与该路径上的信令消息无关。
- 执行此命令时需要确保本端与对端均通过[**ADD SDAPLE**](../Sdup接口业务地址管理/增加SDAP本地实体(ADD SDAPLE)_26147290.md)命令配置SDUP链路的逻辑地址。
- 命令执行过程中如果发生进程复位，探测结果无法保证正确，请在进程正常后再次进行探测。
- 使用此命令需要开启License“82207526 LKV2MCR01 MME链式备份”。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端与对端MME的IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4（IPV4）”<br>- “IPV6（IPV6）”<br>默认值：无 |
| LOCIPV4ADDR | 本端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本端MME IPV4地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV4（IPV4）”<br>时此参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>本参数来源于本端<br>[**ADD SDAPLE**](../Sdup接口业务地址管理/增加SDAP本地实体(ADD SDAPLE)_26147290.md)<br>命令中的<br>“IPv4地址”<br>参数。 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端MME IPV4地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV4（IPV4）”<br>时此参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>本参数来源于对端<br>[**ADD SDAPLE**](../Sdup接口业务地址管理/增加SDAP本地实体(ADD SDAPLE)_26147290.md)<br>命令中的<br>“IPv4地址”<br>参数。 |
| LOCIPV6ADDR | 本端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本端MME IPV6地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV6（IPV6）”<br>时此参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>本参数来源于本端<br>[**ADD SDAPLE**](../Sdup接口业务地址管理/增加SDAP本地实体(ADD SDAPLE)_26147290.md)<br>命令中的<br>“IPv6地址”<br>参数。 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端MME IPV6地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV6（IPV6）”<br>时此参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>本参数来源于对端<br>[**ADD SDAPLE**](../Sdup接口业务地址管理/增加SDAP本地实体(ADD SDAPLE)_26147290.md)<br>命令中的<br>“IPv6地址”<br>参数。 |

## 操作的配置对象

- [测试SDUP路径（SDUPPATH）](configobject/UNC/20.15.2/SDUPPATH.md)

## 使用实例

测试SDUP路径：

TST SDUPPATH: IPTYPE=IPV4, LOCIPV4ADDR="172.16.26.99", PEERIPV4ADDR="172.16.28.99";

```
%%TST SDUPPATH: IPTYPE=IPV4, LOCIPV4ADDR="172.16.26.99", PEERIPV4ADDR="172.16.28.99";%%
RETCODE = 0  操作成功

操作结果如下：
-------------------------
本端地址  =  172.16.26.99
对端地址  =  172.16.28.99
路径状态  =  路径正常
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/测试SDUP路径(TST-SDUPPATH)_01405830.md`
