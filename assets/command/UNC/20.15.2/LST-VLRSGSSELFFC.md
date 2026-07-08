---
id: UNC@20.15.2@MMLCommand@LST VLRSGSSELFFC
type: MMLCommand
name: LST VLRSGSSELFFC（查询VLR的SGs接口自保流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLRSGSSELFFC
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- 自保流控
status: active
---

# LST VLRSGSSELFFC（查询VLR的SGs接口自保流控参数）

## 功能

**适用NF：SMSF**

该命令用于查询VLR的SGs接口自保流控参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [VLR的SGs接口自保流控参数（VLRSGSSELFFC）](configobject/UNC/20.15.2/VLRSGSSELFFC.md)

## 使用实例

运营商希望查询VLR的SGs接口自保流控参数，执行如下命令：

```
LST VLRSGSSELFFC:;
%%LST VLRSGSSELFFC:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
 流控开关 =  开启
位置更新流控响应 =  拥塞拒绝
MO流控响应 =  临时不可达
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR的SGs接口自保流控参数（LST-VLRSGSSELFFC）_04121609.md`
