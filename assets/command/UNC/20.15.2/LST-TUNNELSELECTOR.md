---
id: UNC@20.15.2@MMLCommand@LST TUNNELSELECTOR
type: MMLCommand
name: LST TUNNELSELECTOR（查询隧道选择器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TUNNELSELECTOR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 隧道选择器管理
- 隧道选择器
status: active
---

# LST TUNNELSELECTOR（查询隧道选择器）

## 功能

该命令用于查询隧道选择器。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TUNNELSELECTOR]] · 隧道选择器（TUNNELSELECTOR）

## 使用实例

查询所有配置的隧道选择器信息：

```
LST TUNNELSELECTOR:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
隧道选择器名字  =  a
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TUNNELSELECTOR.md`
