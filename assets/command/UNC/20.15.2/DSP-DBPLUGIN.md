---
id: UNC@20.15.2@MMLCommand@DSP DBPLUGIN
type: MMLCommand
name: DSP DBPLUGIN（查询CSDB插件信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DBPLUGIN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 插件管理
status: active
---

# DSP DBPLUGIN（查询CSDB插件信息）

## 功能

该命令用于显示CSDB插件的信息，包括插件的标识、连接状态、版本号等。

## 注意事项

通过命令 **[DSP DBINSTANCE](../实例管理/查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)** 查询CSDB子实例信息， 返回信息中初始容量和总容量为0时该子实例不支持查询插件信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | 子实例标识 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定特定子实例，可以通过<br>**[DSP DBINSTANCE](../实例管理/查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：1～100。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DBPLUGIN]] · CSDB插件信息（DBPLUGIN）

## 使用实例

查询 “子实例标识” 为 “2” 的插件信息：

DSP DBPLUGIN: INSTANCEID=2;

```
%%DSP DBPLUGIN: INSTANCEID=2;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
子实例标识  虚拟化网络功能组件标识  插件标识  插件连接状态  插件版本号  插件进程所在的资源单元名称  插件进程标识  物理机标识      Pod名称    容器类型         压缩模式                      

2           2                       20000004  稳态          1           CSLB_IP_RU2_0064            1010          1523542645245   sm-pod-1   4GCM Container   关闭
2           2                       20000016  稳态          1           CSLB_IP_RU2_0066            1022          4521542365452   sm-pod-1   4GCM Container   关闭
2           2                       20000009  稳态          1           CSLB_IP_RU2_0065            1015          1523542645245   sm-pod-1   4GCM Container   关闭
2           2                       20000014  稳态          1           CSLB_IP_RU2_0066            1020          1523542645245   sm-pod-1   4GCM Container   关闭
2           2                       20000011  稳态          1           CSLB_IP_RU2_0065            1017          1523542645245   sm-pod-1   4GCM Container   关闭
2           2                       20000006  稳态          1           CSLB_IP_RU2_0064            1012          1523542645245   sm-pod-1   4GCM Container   关闭
(结果个数 = 6)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DBPLUGIN.md`
