---
id: UNC@20.15.2@MMLCommand@LST SGWIPTOSGWPOOL
type: MMLCommand
name: LST SGWIPTOSGWPOOL（查询SGW IP）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGWIPTOSGWPOOL
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 网络管理
- 业务快速恢复
- SGW IP
status: active
---

# LST SGWIPTOSGWPOOL（查询SGW IP）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于显示SGW POOL下绑定的SGW IP。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SGWPOOLNAME | SGW POOL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGW POOL名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>该参数使用ADD SGWPOOL命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGWIPTOSGWPOOL]] · SGW IP（SGWIPTOSGWPOOL）

## 使用实例

假设用户需要查询所有SGW POOL下绑定的SGW IP：

```
%%LST SGWIPTOSGWPOOL:;%%
RETCODE = 0  操作成功

结果如下
--------
 SGW POOL名称  =  sgwpool1
       IP版本  =  IPV4
SGW的IPv4地址  =  10.100.100.100
SGW的IPv6地址  =  ::
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SGWIPTOSGWPOOL.md`
