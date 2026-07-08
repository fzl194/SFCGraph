---
id: UDG@20.15.2@MMLCommand@LST RPTPROTMPCLASS
type: MMLCommand
name: LST RPTPROTMPCLASS（查询业务报表映射承载协议分类配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTPROTMPCLASS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 业务报表管理
- 报表本地策略管理
- 报表映射承载协议分类
status: active
---

# LST RPTPROTMPCLASS（查询业务报表映射承载协议分类配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询业务报表映射承载协议分类信息。当运营商希望查询业务报表映射承载协议分类信息时，则执行该命令。

## 注意事项

如果不输入映射承载协议分类名称，则查询系统所有配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MPPROTCLASSNM | 映射承载协议分类名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置映射承载协议分类名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| MPPROTCLASSIDX | 映射承载协议分类索引 | 可选必选说明：可选参数<br>参数含义：该参数用于设置映射承载协议分类索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTPROTMPCLASS]] · 业务报表映射承载协议分类配置（RPTPROTMPCLASS）

## 使用实例

假如运营商需要查询业务报表映射承载协议分类信息：

```
LST RPTPROTMPCLASS:;
```

```

RETCODE = 0  操作成功。

业务报表映射承载协议分类信息：
--------------------
映射承载协议分类名称    映射承载协议分类索引
p2p                     20
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RPTPROTMPCLASS.md`
