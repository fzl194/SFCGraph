# 查询NG TAI组性能统计对象（LST PERFNGTAIGROUP）

- [命令功能](#ZH-CN_MMLREF_0209652646__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652646__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652646__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652646__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652646__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652646)

**适用NF：AMF、SMF**

该命令用于查询NG TAI组性能统计对象信息。

## [注意事项](#ZH-CN_MMLREF_0209652646)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209652646)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652646)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTAIGPN | NG TAI组名 | 可选必选说明：可选参数<br>参数含义：NG TAI组对外呈现的性能统计名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写，不支持空格及“\”且全局唯一。<br>默认值：无<br>配置原则：无 |
| NGTAIGPTYPE | NG TAI组类型 | 可选必选说明：可选参数<br>参数含义：NG TAI组测量对象的类型。<br>数据来源：本端规划<br>取值范围：<br>- “Manual（手动配置）”：手动配置<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652646)

查询系统配置的所有NG TAI组信息

```
%%LST PERFNGTAIGROUP:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
 NG TAI Group Index  =  1
 NG TAI Group Name  =  huawei
 NG TAI Group Type  =  Manual Configuration
(Number of results = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209652646)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NG TAI组索引 | NG TAI组对应的索引。 |
| NG TAI组名 | NG TAI组对外呈现的性能统计名称。 |
| NG TAI组类型 | NG TAI组测量对象的类型。 |
