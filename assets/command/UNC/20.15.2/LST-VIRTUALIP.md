---
id: UNC@20.15.2@MMLCommand@LST VIRTUALIP
type: MMLCommand
name: LST VIRTUALIP（查询浮动IP）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VIRTUALIP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 地址管理
status: active
---

# LST VIRTUALIP（查询浮动IP）

## 功能

用于查询登录OM Portal的浮动IP类型、浮动IP、网关、子网掩码和前缀长度信息。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VIRTUALIP]] · 浮动IP（VIRTUALIP）

## 使用实例

查询浮动IP信息：

```
%%LST VIRTUALIP:;%%
RETCODE = 0  操作成功

操作结果如下
------------
浮动IP类型  =  IPv4
  IPv4地址  =  192.168.40.47
  IPv4网关  =  192.168.40.1
  子网掩码  =  255.255.255.0
      端口  =  31943
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VIRTUALIP.md`
