---
id: UNC@20.15.2@MMLCommand@LST IPCONVERGENCE
type: MMLCommand
name: LST IPCONVERGENCE（查询Bi口IPCONVERGENCE开关状态）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPCONVERGENCE
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- Bi口IP收敛功能
status: active
---

# LST IPCONVERGENCE（查询Bi口IPCONVERGENCE开关状态）

## 功能

**适用NF：NCG**

该命令用于查询Bi口IPCONVERGENCE开关状态。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPCONVERGENCE]] · Bi口IPCONVERGENCE开关状态（IPCONVERGENCE）

## 使用实例

查询Bi口IPCONVERGENCE开关状态：

```
LST IPCONVERGENCE:;
```

```
RETCODE = 0  操作成功

结果如下:
---------
      Bi口IPCONVERGENCE 开关  =  开启          
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPCONVERGENCE.md`
