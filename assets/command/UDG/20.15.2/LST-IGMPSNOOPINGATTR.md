---
id: UDG@20.15.2@MMLCommand@LST IGMPSNOOPINGATTR
type: MMLCommand
name: LST IGMPSNOOPINGATTR（查询IGMP Snooping属性配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IGMPSNOOPINGATTR
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- IGMP Snooping配置
- IGMP Snooping属性配置
status: active
---

# LST IGMPSNOOPINGATTR（查询IGMP Snooping属性配置）

## 功能

**适用NF：UPF**

该命令用于查询指定5G LAN组的IGMP Snooping属性配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD NGVNINSTANCE命令配置生成。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IGMPSNOOPINGATTR]] · IGMP Snooping属性配置（IGMPSNOOPINGATTR）

## 使用实例

查询指定5G LAN组的IGMP Snooping功能相关属性：

```
LST IGMPSNOOPINGATTR: VNINSTANCE="a0000001-460-003-02";
```

```

%%LST IGMPSNOOPINGATTR: VNINSTANCE="a0000001-460-003-02";%%
RETCODE = 0 操作成功

IGMP Snooping属性配置
-------------------------------------
                  5G LAN组名称  =  a0000001-460-003-02
                查询器功能开关  =  ENABLE
      普遍组查询时间间隔（秒）  =  60
普遍组查询的最大响应时间（秒）  =  10
                  IGMP健壮系数  =  2
  IGMP普遍组查询报文的源IP地址  =  10.2.3.4
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IGMPSNOOPINGATTR.md`
