---
id: UDG@20.15.2@MMLCommand@LST TAIGROUP
type: MMLCommand
name: LST TAIGROUP（查看指定TAI组或者已配置所有TAI组的配置信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TAIGROUP
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- TAI组
status: active
---

# LST TAIGROUP（查看指定TAI组或者已配置所有TAI组的配置信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查看指定TAI组或者所有TAI组的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIGROUPNAME | 指定TAI组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TAI组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TAIGROUP]] · 指定的TAI组（TAIGROUP）

## 使用实例

假设运营商需要去查询指定TAI组beijing：

```
LST TAIGROUP: TAIGROUPNAME="beijing";
```

```
 RETCODE = 0 操作成功。 结果如下
TAI组
-----------------------
指定TAI组名  =  beijing
 TAC 类型  =  N2TAC
 移动国家码 =  456
 移动网络号  =  789
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TAIGROUP.md`
