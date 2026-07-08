---
id: UNC@20.15.2@MMLCommand@LST ALLOWSERNAME
type: MMLCommand
name: LST ALLOWSERNAME（查询基于地址的白名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ALLOWSERNAME
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- 白名单管理
- 基于地址的白名单管理
status: active
---

# LST ALLOWSERNAME（查询基于地址的白名单）

## 功能

该命令用于查询基于服务地址的NF实例的服务白名单信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定白名单索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ALLOWSERNAME]] · 基于地址的白名单（ALLOWSERNAME）

## 使用实例

查询所有配置的基于服务地址的服务白名单信息。

```
%%LST ALLOWSERNAME:;%%
RETCODE = 0  操作成功

结果如下
--------
      索引  =  0
NF实例标识  =  SMF_Instance_0
  服务名称  =  nsmfP dusess
  本端地址  =  192.168.0.1
  对端地址  =  192.168.0.2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ALLOWSERNAME.md`
