---
id: UNC@20.15.2@MMLCommand@LST CEAORIGHOSTCHK
type: MMLCommand
name: LST CEAORIGHOSTCHK（查询对Gy接口的cea消息中的Origin-Host检查开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CEAORIGHOSTCHK
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 公共参数
- Diameter公共参数
status: active
---

# LST CEAORIGHOSTCHK（查询对Gy接口的cea消息中的Origin-Host检查开关）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询Diameter对Gy接口的cea消息中的Origin-Host检查开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [对Gy接口的cea消息中的Origin-Host检查开关（CEAORIGHOSTCHK）](configobject/UNC/20.15.2/CEAORIGHOSTCHK.md)

## 使用实例

查询Diameter对Gy接口的cea消息中的Origin-Host检查开关，则可按如下配置：

```
LST CEAORIGHOSTCHK:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
检查Gy的CEA消息中的Origin-Host  =  禁止
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询对Gy接口的cea消息中的Origin-Host检查开关（LST-CEAORIGHOSTCHK）_09897241.md`
