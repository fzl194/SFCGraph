---
id: UNC@20.15.2@MMLCommand@LST EXEMPTSERVICE
type: MMLCommand
name: LST EXEMPTSERVICE（查询豁免业务）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EXEMPTSERVICE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 分组数据离线状态管理
- 豁免业务配置
status: active
---

# LST EXEMPTSERVICE（查询豁免业务）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询豁免业务。豁免业务（3GPP PS data off Exempt Services）不受3GPP PS data off能力控制，即使3GPP PS data off能力使能，这类业务也不受影响。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [豁免业务（EXEMPTSERVICE）](configobject/UNC/20.15.2/EXEMPTSERVICE.md)

## 使用实例

当运营商需要查询豁免业务，执行如下命令：

```
%%LST EXEMPTSERVICE:;%%
RETCODE = 0  操作成功

结果如下
--------
豁免APN  =  huawei.com
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询豁免业务（LST-EXEMPTSERVICE）_81398991.md`
