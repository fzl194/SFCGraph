---
id: UDG@20.15.2@MMLCommand@LST TAIGROUPBINDING
type: MMLCommand
name: LST TAIGROUPBINDING（查看TAI组绑定的TAC号段）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TAIGROUPBINDING
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- TAI组与TAI号段绑定关系
status: active
---

# LST TAIGROUPBINDING（查看TAI组绑定的TAC号段）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查看TAI组绑定的TAC号段。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIGROUPNAME | 指定TAI组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TAI组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD TAIGROUP命令配置生成。 |

## 操作的配置对象

- [TAC号段与TAI组的绑定关系（TAIGROUPBINDING）](configobject/UDG/20.15.2/TAIGROUPBINDING.md)

## 使用实例

假设运营商需要查看指定TAC号段与TAI组的绑定关系：TAI组为beijing，TAC号段为0：

```
LST TAIGROUPBINDING:;
```

```

RETCODE = 0  操作成功

TAI组与TAI号段绑定关系
-------------------------------
    指定TAI组名  =  beijing
      TAC起始ID  =  0x000000
      TAC截止ID  =  0x000010
    TAC 段编号  =  0
(返回个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查看TAI组绑定的TAC号段（LST-TAIGROUPBINDING）_26089117.md`
