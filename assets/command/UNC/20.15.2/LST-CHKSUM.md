---
id: UNC@20.15.2@MMLCommand@LST CHKSUM
type: MMLCommand
name: LST CHKSUM（查询校验和开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHKSUM
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 校验和开关管理
status: active
---

# LST CHKSUM（查询校验和开关）

## 功能

**适用NF：NCG**

该命令用于查询UDP校验和校验开关。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHKSUM]] · 校验和开关（CHKSUM）

## 使用实例

查询UDP校验和校验开关：

```
LST CHKSUM:;
```

```
RETCODE = 0  操作成功。

结果如下:
--------
             网络用途  =  Ga
接收UDP校验和校验开关  =  关闭
发送UDP校验和校验开关  =  关闭
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHKSUM.md`
