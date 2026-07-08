---
id: UNC@20.15.2@MMLCommand@LST ACLGROUP6IPSEC
type: MMLCommand
name: LST ACLGROUP6IPSEC（查询IPv6 ACL规则组配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ACLGROUP6IPSEC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- ACL管理
- IPv6 ACL规则组
status: active
---

# LST ACLGROUP6IPSEC（查询IPv6 ACL规则组配置）

## 功能

该命令用于查询系统内已经配置的ACL规则组的信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | 规则组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是3000～3999（高级ACL），但兼容CE版本，允许配置其他数值但不会生效。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ACLGROUP6IPSEC]] · IPv6 ACL规则组（ACLGROUP6IPSEC）

## 使用实例

查询当前设备上所有的规则组信息，不输入ACLNAME：

```
RETCODE = 0  操作成功。

结果如下
--------
ACL规则组标识    规则组步长    规则组类型    规则的匹配顺序                    规则组描述

3000             5             高级ACL       规则组下的规则按照配置优先排序    NULL    
3005             5             高级ACL       规则组下的规则按照配置优先排序    NULL      
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ACLGROUP6IPSEC.md`
