---
id: UNC@20.15.2@MMLCommand@LST HTTPNFINST
type: MMLCommand
name: LST HTTPNFINST（查询HTTP服务存储的NF实例信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPNFINST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP平台管理
status: active
---

# LST HTTPNFINST（查询HTTP服务存储的NF实例信息）

## 功能

该命令用于查询HTTP服务存储的NF实例信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HTTPNFINST]] · HTTP服务存储的NF实例信息（HTTPNFINST）

## 使用实例

维护人员需要查询HTTP服务存储的NF实例信息时，可使用如下命令：

```
LST HTTPNFINST:;
%%LST HTTPNFINST:;%%
RETCODE = 0  操作成功

结果如下
------------------------
NF类型       NF实例名称        NF实例标识

NFTypeNRF    NRF_Instance_0    00000000-0000-0000-0000-000000000013
NFTypeAMF    AMF_Instance_0    00000000-0000-0000-0000-000000000011
NFTypeSMF    SMF_Instance_0    00000000-0000-0000-0000-000000000012
NFTypeNSSF   NSSF_Instance_0   00000000-0000-0000-0000-000000000014
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HTTPNFINST.md`
