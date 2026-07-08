---
id: UNC@20.15.2@MMLCommand@LST PERFDNAI
type: MMLCommand
name: LST PERFDNAI（查询用于性能统计的数据网络访问标识信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFDNAI
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# LST PERFDNAI（查询用于性能统计的数据网络访问标识信息）

## 功能

**适用NF：SMF**

该命令用于查询可用于性能统计的数据网络访问标识信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFDNAI]] · 用于性能统计的数据网络访问标识信息（PERFDNAI）

## 使用实例

查询所有可用于性能统计的数据网络访问标识信息，执行如下命令：

```
%%LST PERFDNAI:;%%
RETCODE = 0  操作成功

结果如下
 --------
数据网络访问标识  =  huawei.com
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用于性能统计的数据网络访问标识信息（LST-PERFDNAI）_68161917.md`
