---
id: UDG@20.15.2@MMLCommand@SET PREFIXURLPARA
type: MMLCommand
name: SET PREFIXURLPARA（设置前缀URL匹配时的控制参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PREFIXURLPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 105000
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- 前缀URL参数
status: active
---

# SET PREFIXURLPARA（设置前缀URL匹配时的控制参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置前缀URL匹配时的控制开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为105000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |
| CHECKDESTURL | 匹配Server IP的开关 | 可选必选说明：必选参数<br>参数含义：指定是否需要将前缀URL与报文的Server IP进行匹配。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：当需要控制PrefixUrl匹配流程中，是否需要检查IP地址格式，并且匹配Server IP时，设置此参数为Enable。 |
| CHECKSCHEME | 检查Scheme开关 | 可选必选说明：必选参数<br>参数含义：指定是否需要在匹配prefix url之前先检查path是否以Scheme开头。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：当需要控制PrefixUrl匹配流程中，需要判断PATH以http://或者https://开头时，配置此参数为使能。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PREFIXURLPARA]] · 前缀URL参数（PREFIXURLPARA）

## 使用实例

为用户模板配置前缀URL参数，使能检查目的IP：

```
SET PREFIXURLPARA: USERPROFILENAME="testprofile1", CHECKDESTURL=ENABLE, CHECKSCHEME=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PREFIXURLPARA.md`
