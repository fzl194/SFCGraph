---
id: UNC@20.15.2@MMLCommand@DSP KPIRES
type: MMLCommand
name: DSP KPIRES（显示关键资源信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: KPIRES
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- 通用调测
status: active
---

# DSP KPIRES（显示关键资源信息）

## 功能

显示关键资源信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ID | 资源ID | 可选必选说明：必选参数<br>参数含义：资源ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| PODNAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是3~100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@KPIRES]] · 关键资源信息（KPIRES）

## 使用实例

查询“资源ID”为“10001”的资源信息，执行如下命令：

```
%%DSP KPIRES: ID=10001;%%
RETCODE = 0  操作成功

结果如下
--------
资源ID  资源描述                   Pod名称    分区  使用量  规格  

10001   s6b: active do in do pool  sm2-pod-0  2     0       3000  
10001   s6b: active do in do pool  sm2-pod-0  4     0       3000 
(结果个数 = 2)

---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-KPIRES.md`
