---
id: UNC@20.15.2@MMLCommand@LST RESTOUSR
type: MMLCommand
name: LST RESTOUSR（查询容灾用户特征参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESTOUSR
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME容灾管理
- 容灾用户特征管理
status: active
---

# LST RESTOUSR（查询容灾用户特征参数）

## 功能

**适用网元：MME**

本命令用于查询支持容灾备份的用户特征。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTOUSR]] · 容灾用户特征参数（RESTOUSR）

## 使用实例

查询支持容灾备份的用户特征记录：

LST RESTOUSR:;

```
%%LST RESTOUSR:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
IMSI前缀  =  12303
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询容灾用户特征参数(LST-RESTOUSR)_26146118.md`
