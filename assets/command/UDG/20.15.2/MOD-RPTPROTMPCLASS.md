---
id: UDG@20.15.2@MMLCommand@MOD RPTPROTMPCLASS
type: MMLCommand
name: MOD RPTPROTMPCLASS（修改业务报表映射承载协议分类配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: RPTPROTMPCLASS
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务报表管理
- 报表本地策略管理
- 报表映射承载协议分类
status: active
---

# MOD RPTPROTMPCLASS（修改业务报表映射承载协议分类配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改业务报表映射承载协议分类配置。

## 注意事项

- 该命令执行后立即生效。
- 如果引用了该业务报表映射承载协议分类配置的映射记录存在，则仅允许修改映射承载协议分类索引参数，修改后的承载协议分类索引与其他映射承载协议分类配置中的承载协议分类索引不冲突。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MPPROTCLASSNM | 映射承载协议分类名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置映射承载协议分类名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| MPPROTCLASSIDX | 映射承载协议分类索引 | 可选必选说明：必选参数<br>参数含义：该参数用于设置映射承载协议分类索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTPROTMPCLASS]] · 业务报表映射承载协议分类配置（RPTPROTMPCLASS）

## 使用实例

假如运营商需要修改一个业务报表映射承载协议分类配置中的映射承载协议分类索引值为20：

```
MOD RPTPROTMPCLASS: MPPROTCLASSNM="p2p", MPPROTCLASSIDX=20;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-RPTPROTMPCLASS.md`
