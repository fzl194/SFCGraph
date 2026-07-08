---
id: UDG@20.15.2@MMLCommand@LST UPNON3GPPPARA
type: MMLCommand
name: LST UPNON3GPPPARA（查询非3GPP业务配置参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPNON3GPPPARA
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 非3GPP业务管理
status: active
---

# LST UPNON3GPPPARA（查询非3GPP业务配置参数）

## 功能

**适用NF：UPF**

该命令用来查询非3GPP业务配置参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [非3GPP业务配置参数（UPNON3GPPPARA）](configobject/UDG/20.15.2/UPNON3GPPPARA.md)

## 使用实例

查询非3GPP业务配置参数：

```
LST UPNON3GPPPARA:;
```

```

RETCODE = 0  操作成功。

结果如下:
---------
      SWU接口UE接入速率  =  1000
ToH SESSION的老化时长  =  1440
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询非3GPP业务配置参数（LST-UPNON3GPPPARA）_56514301.md`
