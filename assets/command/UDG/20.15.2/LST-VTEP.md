---
id: UDG@20.15.2@MMLCommand@LST VTEP
type: MMLCommand
name: LST VTEP（查询VXLAN隧道端点）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VTEP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VXLAN隧道端点配置
status: active
---

# LST VTEP（查询VXLAN隧道端点）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询VXLAN隧道端点信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VTEPNAME | VXLAN隧道端点名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置VXLAN隧道端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VTEP]] · VXLAN隧道端点（VTEP）

## 使用实例

查询所有隧道端点的相关信息：

```
LST VTEP:;
```

```

RETCODE = 0 操作成功。

VXLAN隧道端点信息
-----------------
VXLAN隧道端点名称  =  vtep1            
IP协议版本  =  IPV4 
隧道对端端点的IPv4地址  =  192.168.1.1
隧道对端端点的IPv6地址  =  ::
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VTEP.md`
