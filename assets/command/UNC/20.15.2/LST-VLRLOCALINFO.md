---
id: UNC@20.15.2@MMLCommand@LST VLRLOCALINFO
type: MMLCommand
name: LST VLRLOCALINFO（查询VLR的本局信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLRLOCALINFO
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- VLR本局信息管理
status: active
---

# LST VLRLOCALINFO（查询VLR的本局信息）

## 功能

**适用NF：SMSF**

该命令用于查询VLR的本局信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLRLOCALINFO]] · VLR的本局信息（VLRLOCALINFO）

## 使用实例

运营商希望查询VLR的NRI等本局信息，执行如下命令：

```
LST VLRLOCALINFO:;
%%LST VLRLOCALINFO:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
        VLR的网络资源标识 =  1
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VLRLOCALINFO.md`
