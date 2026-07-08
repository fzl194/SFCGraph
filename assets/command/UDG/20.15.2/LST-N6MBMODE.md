---
id: UDG@20.15.2@MMLCommand@LST N6MBMODE
type: MMLCommand
name: LST N6MBMODE（查询N6mb接口数据传输的优选方式及端口配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: N6MBMODE
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- MBS管理
- N6mb接口模式配置
status: active
---

# LST N6MBMODE（查询N6mb接口数据传输的优选方式及端口配置）

## 功能

**适用NF：UPF**

该命令用于查询N6mb接口的数据传输的优选方式及端口范围。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/N6MBMODE]] · N6mb接口数据传输的优选方式及端口配置（N6MBMODE）

## 使用实例

查询N6mb接口数据传输的优选方式及端口配置：

```
LST N6MBMODE:;
```

```

RETCODE = 0  操作成功

N6mb接口数据传输方式配置
-----------------------------------------------------
N6mb接口数据传输的优选方式  =  unicast
           起始的UDP端口号  =  1024
           结束的UDP端口号  =  4023
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询N6mb接口数据传输的优选方式及端口配置（LST-N6MBMODE）_47981249.md`
