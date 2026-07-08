---
id: UNC@20.15.2@MMLCommand@LST CHARGEMETHOD
type: MMLCommand
name: LST CHARGEMETHOD（查询计费方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHARGEMETHOD
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 计费属性计费控制
status: active
---

# LST CHARGEMETHOD（查询计费方式）

## 功能

**适用NF：PGW-C、SMF**

此命令用来查询基于用户计费属性配置在线计费和离线计费方式。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [计费方式（CHARGEMETHOD）](configobject/UNC/20.15.2/CHARGEMETHOD.md)

## 使用实例

查询所有用户的在线计费和离线计费方式信息：

```
LST CHARGEMETHOD:;
```

```

RETCODE = 0  操作成功

计费方式
--------
      计费属性值  =  0x0000
    计费属性掩码  =  0xFFFF
  计费属性优先级  =  0
    在线计费开关  =  禁止
    离线计费开关  =  允许
    融合计费开关  =  允许
        计费属性  =  缺省
业务申请上报模式  =  融合业务申请上报模式
     QBC计费开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询计费方式（LST-CHARGEMETHOD）_09896798.md`
