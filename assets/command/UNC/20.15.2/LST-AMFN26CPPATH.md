---
id: UNC@20.15.2@MMLCommand@LST AMFN26CPPATH
type: MMLCommand
name: LST AMFN26CPPATH（查询AMF N26消息抄送路径）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFN26CPPATH
command_category: 查询类
applicable_nf:
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- N26互操作管理
- N26消息抄送路径
status: active
---

# LST AMFN26CPPATH（查询AMF N26消息抄送路径）

## 功能

**适用网元：MME、AMF**

该命令用于查询AMF N26消息抄送路径相关的参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug。
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组。

## 参数

无。

## 操作的配置对象

- [AMF N26消息抄送路径（AMFN26CPPATH）](configobject/UNC/20.15.2/AMFN26CPPATH.md)

## 使用实例

查询AMF N26消息抄送路径：

LST AMFN26CPPATH:;

```
%%LST AMFN26CPPATH:;%%
RETCODE = 0  操作成功

输出结果如下
------------------------
        抄送路径开关  =  打开
          IP地址类型  =  IPV4类型
       MME侧IPv4地址  =  192.168.1.1
       MME侧IPv6地址  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
       AMF侧IPv4地址  =  192.168.2.2
       AMF侧IPv6地址  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
             VPN名称  =  _abc_
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF-N26消息抄送路径（LST-AMFN26CPPATH）_29829116.md`
