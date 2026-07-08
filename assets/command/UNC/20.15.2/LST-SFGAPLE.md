---
id: UNC@20.15.2@MMLCommand@LST SFGAPLE
type: MMLCommand
name: LST SFGAPLE（查询SFGAP本端实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SFGAPLE
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- SFGAP本端实体管理
status: active
---

# LST SFGAPLE（查询SFGAP本端实体）

## 功能

**适用NF：AMF**

在部署感知的场景下，通过LST SFGAPLE查询SFGAP本端实体信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SFGAPLEIDX | SFGAP本端实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SFGAP本端实体的索引，该索引作为SFGAP本端实体的唯一标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFGAPLE]] · SFGAP本端实体（SFGAPLE）

## 使用实例

输入SFGAP本端实体标识，查询指定的SFGAP本端实体，执行如下命令：

```
%%LST SFGAPLE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
 SFGAP本端实体索引  =  1
SCTP本端实体组标识  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SFGAP本端实体（LST-SFGAPLE）_75822980.md`
