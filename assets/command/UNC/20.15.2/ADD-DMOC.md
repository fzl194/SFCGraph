---
id: UNC@20.15.2@MMLCommand@ADD DMOC
type: MMLCommand
name: ADD DMOC（增加Diameter流控节点）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DMOC
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- Diameterl流控管理
status: active
---

# ADD DMOC（增加Diameter流控节点）

## 功能

**适用网元：SGSN、MME**

该命令用于增加Diameter流控节点，在对端Diameter启动流控后，通过该命令增加支持流控的配置信息。

配置规则：根据Diameter流控节点类型不同进行添加。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为1000。
- Diameter流控是RFC7683中定义的流控机制，当前该流控机制仅支持S6a接口。
- S6a口选路为域路由时，该命令中仅配置该路由的主机名，需同时配置该路由对应的域名。
- 系统影响：本流控启动后，USN会丢弃部分S6A口的ULR、AIR、PUR、NOR消息。
- HOSTNAME和REALMNAME参数不区分大小写，转大写存储。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter流控节点的索引。<br>数据来源：本端规划<br>取值范围：整数范围1~1000<br>默认值： 无<br>配置原则：无 |
| TYPE | 类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter流控节点的类型。<br>数据来源：整网规划<br>取值范围：枚举值。<br>- “BYHOSTNAME(基于主机名)”<br>- “BYREALMNAME(基于域名)”<br>默认值：无<br>配置原则：<br>- “BYHOSTNAME(基于主机名)”：配置主机名，表示基于对端实体主机名进行Diameter流控。<br>- “BYREALMNAME(基于域名)”：配置域名，表示基于对端实体域名进行Diameter流控。 |
| HOSTNAME | 主机名 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定Diameter流控节点的主机名。<br>前提条件：该参数在<br>“TYPE”<br>设置为<br>“BYHOSTNAME(基于主机名)”<br>后生效。<br>数据来源：整网规划<br>取值范围：长度为1~127位的字符串<br>默认值：无<br>配置原则：<br>- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。例如：epc.mnc015.mcc234.3gppnetwork.org。<br>- 该参数不能设置重复值。 |
| REALMNAME | 域名 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定Diameter流控节点的域名。<br>前提条件：该参数在<br>“TYPE”<br>设置为<br>“BYREALMNAME(基于域名)”<br>后生效。<br>数据来源：整网规划<br>取值范围：长度为1~127位的字符串<br>默认值：无<br>配置原则：<br>- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。例如：epc.mnc015.mcc234.3gppnetwork.org。<br>- 该参数不能设置重复值。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DMOC]] · Diameter流控节点（DMOC）

## 使用实例

增加一个类型为主机名的Diameter流控节点和增加一个类型为域名的Diameter流控节点：

ADD DMOC: INDEX=1, TYPE=BYHOSTNAME, HOSTNAME="epc.mnc015.mcc234.3gppnetwork.org";

ADD DMOC: INDEX=2, TYPE=BYREALMNAME, REALMNAME="epc.mnc015.mcc234.3gppnetwork.org";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DMOC.md`
