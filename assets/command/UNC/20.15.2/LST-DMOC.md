---
id: UNC@20.15.2@MMLCommand@LST DMOC
type: MMLCommand
name: LST DMOC（查询Diameter流控节点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DMOC
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
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

# LST DMOC（查询Diameter流控节点）

## 功能

**适用网元：SGSN、MME**

该命令用于查询Diameter流控节点信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter流控节点的索引。<br>数据来源：本端规划<br>取值范围：整数范围1~1000<br>默认值： 无<br>配置原则：无 |
| TYPE | 类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter流控节点的类型。<br>数据来源：整网规划<br>取值范围：枚举值。<br>- “BYHOSTNAME(基于主机名)”<br>- “BYREALMNAME(基于域名)”<br>默认值：无<br>配置原则：<br>- “BYHOSTNAME(基于主机名)”：配置主机名，表示基于对端实体主机名进行Diameter流控。<br>- “BYREALMNAME(基于域名)”：配置域名，表示基于对端实体域名进行Diameter流控。 |
| HOSTNAME | 主机名 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定Diameter流控节点的主机名。<br>前提条件：该参数在<br>“TYPE”<br>设置为<br>“BYHOSTNAME(基于主机名)”<br>后生效。<br>数据来源：整网规划<br>取值范围：长度为1~127位的字符串<br>默认值：无<br>配置原则：<br>- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。例如：epc.mnc015.mcc234.3gppnetwork.org。 |
| REALMNAME | 域名 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定Diameter流控节点的域名。<br>前提条件：该参数在<br>“TYPE”<br>设置为<br>“BYREALMNAME(基于域名)”<br>后生效。<br>数据来源：整网规划<br>取值范围：长度为1~127位的字符串<br>默认值：无<br>配置原则：<br>- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。例如：epc.mnc015.mcc234.3gppnetwork.org。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DMOC]] · Diameter流控节点（DMOC）

## 使用实例

1. 查询所有Diameter流控节点记录：
  LST DMOC:;
2. 查询索引为1的Diameter流控节点记录：
  LST DMOC: INDEX=1;
3. 查询主机名类型的Diameter流控节点记录（域名同理）：
  LST DMOC: TYPE=BYHOSTNAME;
4. 查询类型为BYHOSTNAME主机名为ewre的Diameter流控节点记录（域名同理）：
  LST DMOC: TYPE=BYHOSTNAME, HOSTNAME="epc.mnc015.mcc234.3gppnetwork.org";

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DMOC.md`
