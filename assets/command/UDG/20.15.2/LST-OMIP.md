---
id: UDG@20.15.2@MMLCommand@LST OMIP
type: MMLCommand
name: LST OMIP（查询OM IP）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OMIP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 代理管理
status: active
---

# LST OMIP（查询OM IP）

## 功能

用于查询OM网络配置。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/OMIP]] · OM IP（OMIP）

## 使用实例

查询OMIP：

```
%%LST OMIP:;%%
RETCODE = 0  操作成功
IPv4浮动IP信息如下
------------------
  IP地址  =  10.144.246.179
    端口  =  31943
子网掩码  =  255.255.255.0
默认网关  =  10.144.246.254
(结果个数 = 1)

IPv6浮动IP信息如下
------------------
  IP地址  =  2001:db8:0000:4202:0156:0110:0202:0511
    端口  =  31943
前缀长度  =  64
默认网关  =  2001:db8:0000:4202:0156:0110:0202:0254
(结果个数 = 1)

物理IP信息如下
--------------
主机名  IP地址                         

host1   2001:db8:0:4202:156:110:202:191  
host2   10.144.246.202                
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OM-IP-(LST-OMIP)_76163349.md`
