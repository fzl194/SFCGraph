---
id: UNC@20.15.2@MMLCommand@LST ROUTSMSCPARA
type: MMLCommand
name: LST ROUTSMSCPARA（查询SMSF/VLR选择SMSC的相关参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ROUTSMSCPARA
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- SMSC选择管理
status: active
---

# LST ROUTSMSCPARA（查询SMSF/VLR选择SMSC的相关参数）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF/VLR选择SMSC的相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [SMSF/VLR选择SMSC的相关参数（ROUTSMSCPARA）](configobject/UNC/20.15.2/ROUTSMSCPARA.md)

## 使用实例

运营商希望查询SMSF/VLR选择SMSC的相关参数，执行如下命令：

```
LST ROUTSMSCPARA:;
%%LST ROUTSMSCPARA:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
        本大区SMSC的虚拟GT        =  123456
        按号段选择SMSC开关  =  打开
        本大区异DC部署的SMSC的真实GT = 1234567
        MSISDN匹配长度          = 4
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMSF_VLR选择SMSC的相关参数（LST-ROUTSMSCPARA）_04281133.md`
