---
id: UDG@20.15.2@MMLCommand@LST GLBDLLTBUFFER
type: MMLCommand
name: LST GLBDLLTBUFFER（查询全局下行数据长时间缓存配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBDLLTBUFFER
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- GTP隧道管理
- 全局下行数据长时间缓存
status: active
---

# LST GLBDLLTBUFFER（查询全局下行数据长时间缓存配置）

## 功能

**适用NF：UPF**

此命令用来查询全局的用户下行数据长时间缓存配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBDLLTBUFFER]] · 全局下行数据长时间缓存配置（GLBDLLTBUFFER）

## 使用实例

查询全局下行报文长时间缓存的配置：

```
LST GLBDLLTBUFFER:;
```

```

RETCODE = 0  操作成功

下行数据长时间缓存全局配置
--------------------------
最大缓存个数  =  1
    存储方式  =  环形存储
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBDLLTBUFFER.md`
