---
id: UNC@20.15.2@MMLCommand@LST SMSFUDMRESET
type: MMLCommand
name: LST SMSFUDMRESET（查询UDM重选参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFUDMRESET
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- UDM重选管理
status: active
---

# LST SMSFUDMRESET（查询UDM重选参数）

## 功能

**适用NF：SMSF**

该命令用来查询SMSF的UDM重选参数信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [SMSF的UDM重选（SMSFUDMRESET）](configobject/UNC/20.15.2/SMSFUDMRESET.md)

## 使用实例

运营商希望查询SMSF的UDM扫描任务重选开关是否开启，执行如下命令：

```
%%LST SMSFUDMRESET:;%%
RETCODE = 0  操作成功

结果如下
------------------------
      是否触发扫描任务重选UDM  =  是
       UDM重选扫描速率(个/秒)  =  5
UDM重选时是否重新获取签约数据  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UDM重选参数（LST-SMSFUDMRESET）_99973534.md`
