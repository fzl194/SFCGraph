---
id: UNC@20.15.2@MMLCommand@LST APNNIGROUP
type: MMLCommand
name: LST APNNIGROUP（查询APNNI组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNNIGROUP
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APNNI信息管理
- APNNI组管理
status: active
---

# LST APNNIGROUP（查询APNNI组）

## 功能

**适用网元：SGSN、MME**

该命令用于查询APNNI组信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNNIGROUP]] · APNNI组（APNNIGROUP）

## 使用实例

查询APNNI组信息：

LST APNNIGROUP:;

```
%%LST APNNIGROUP:;%%
输出结果如下
--------------
APNNI组号  =  2
     描述  =  M2M APNNI Group
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNNIGROUP.md`
