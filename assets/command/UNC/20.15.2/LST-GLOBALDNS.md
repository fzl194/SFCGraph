---
id: UNC@20.15.2@MMLCommand@LST GLOBALDNS
type: MMLCommand
name: LST GLOBALDNS（查询系统默认DNS）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLOBALDNS
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- DNS选择管理
- 缺省DNS
status: active
---

# LST GLOBALDNS（查询系统默认DNS）

## 功能

**适用NF：SMF**

该命令用来查看系统默认的DNS属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLOBALDNS]] · 系统默认DNS（GLOBALDNS）

## 使用实例

查询系统的默认的DNS属性：

```
%%LST GLOBALDNS:;%%
RETCODE = 0  操作成功

结果如下
--------
        IPv6主DNS服务器IP  =  2001:0DB8:0:1::
        IPv6备DNS服务器IP  =  2001:0DB8:0:2::
        IPv4主DNS服务器IP  =  10.1.1.1
        IPv4备DNS服务器IP  =  10.2.2.2
IPv4 第一优先级服务器属性  =  dhcp
IPv4 第二优先级服务器属性  =  radius
IPv6 第一优先级服务器属性  =  dhcp
IPv6 第二优先级服务器属性  =  radius
      IPv6主DNS64服务器IP  =  2001:0DB8:0:3::
      IPv6备DNS64服务器IP  =  2001:0DB8:0:4::
IPv4 第三优先级服务器属性  =  local
IPv4 第四优先级服务器属性  =  pcrf
IPv6 第三优先级服务器属性  =  local
IPv6 第四优先级服务器属性  =  pcrf
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询系统默认DNS（LST-GLOBALDNS）_09651751.md`
