---
id: UNC@20.15.2@MMLCommand@LST APNNIDT
type: MMLCommand
name: LST APNNIDT（查询APNNI Direct Tunnel配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNNIDT
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- Direct Tunnel管理
status: active
---

# LST APNNIDT（查询APNNI Direct Tunnel配置）

## 功能

**适用网元：SGSN**

此命令用于查询APNNI DT属性信息表中的某个APNNI的DT属性信息。

## 注意事项

- 此命令执行后立即生效。
- 用户要使用DT功能还需满足RNC、GGSN和IMSI支持DT功能。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定启用基于APNNI的DT功能的APNNI。<br>取值范围：1～62位字符串<br>默认值：无<br>说明：“APNNI”<br>（APN网络标识地址）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A~Z或a~z、数字0~9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。“*”表示通配符，如果用户使用的APNNI在配置表中无法匹配到对应的记录，则查询“*”通配符对应的配置记录。如果查询成功则使用“*”对应的配置；如果查询失败，则默认支持DT。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNNIDT]] · APNNI Direct Tunnel配置（APNNIDT）

## 使用实例

查询某个APNNI的DT属性记录：

LST APNNIDT: APNNI="huawei.com";

```
%%LST APNNIDT: APNNI="huawei.com";%%
RETCODE = 0  操作成功。

APNNI DT属性配置列表
--------------------
            APNNI  =  HUAWEI.COM
启用Direct Tunnel  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APNNI-Direct-Tunnel配置(LST-APNNIDT)_26305856.md`
