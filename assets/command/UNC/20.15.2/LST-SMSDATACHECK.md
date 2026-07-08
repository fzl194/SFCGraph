---
id: UNC@20.15.2@MMLCommand@LST SMSDATACHECK
type: MMLCommand
name: LST SMSDATACHECK（查询数据核查扫描参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSDATACHECK
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 数据核查
status: active
---

# LST SMSDATACHECK（查询数据核查扫描参数）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF数据核查扫描速率和周期，以及SMSF数据有效时长。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSDATACHECK]] · 数据核查扫描参数（SMSDATACHECK）

## 使用实例

查询sms数据核查扫描速率及用户数据有效时长，执行如下命令：

```
LST SMSDATACHECK:;
%%LST SMSDATACHECK:;%%
RETCODE = 0  操作成功
结果如下:
------------------------
       sms数据核查速率(个每秒)  =  5
         sms数据核查周期(分钟)  =  30
          SMSF数据有效时长开关  =  FUNC_ON
SMSF上用户数据的有效时长(小时)  =  48
               UDM数据核查开关  =  FUNC_ON
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSDATACHECK.md`
