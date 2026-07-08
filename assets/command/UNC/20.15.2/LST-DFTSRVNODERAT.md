---
id: UNC@20.15.2@MMLCommand@LST DFTSRVNODERAT
type: MMLCommand
name: LST DFTSRVNODERAT（查询默认RAT类型）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DFTSRVNODERAT
command_category: 查询类
applicable_nf:
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取RAT管理
- 全局RAT配置
status: active
---

# LST DFTSRVNODERAT（查询默认RAT类型）

## 功能

**适用NF：GGSN**

该命令用来查看默认所属的RAT类型。获取RAT类型用于从虚拟APN映射到真实APN、匹配user-profile进行业务、计费控制。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数表示当前配置的网元类型。<br>数据来源：本端规划<br>取值范围：<br>- GGSN（GGSN）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [默认RAT类型（DFTSRVNODERAT）](configobject/UNC/20.15.2/DFTSRVNODERAT.md)

## 使用实例

查询默认的RAT类型：

```
%%LST DFTSRVNODERAT:;%%
RETCODE = 0  操作成功

结果如下
--------
网元类型  =  GGSN
 RAT类型  =  NONE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询默认RAT类型（LST-DFTSRVNODERAT）_09652266.md`
