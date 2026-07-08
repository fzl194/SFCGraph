---
id: UDG@20.15.2@MMLCommand@DSP MSSWPREC
type: MMLCommand
name: DSP MSSWPREC（显示微服务主实例切换历史记录）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSWPREC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP MSSWPREC（显示微服务主实例切换历史记录）

## 功能

该命令用于查询微服务主备倒换历史记录，支持基于服务名称查询或者查询全部微服务。查询全部微服务时默认按切换时间排序，显示离查询时间最近的前100条记录。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 微服务名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示微服务的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>可通过<br>[**DSP MSACTIVE**](显示服务主实例相关信息（DSP MSACTIVE）_88183810.md)<br>命令获取返回结果中的Cell Service Name作为参数输入。 |

## 操作的配置对象

- [微服务主实例切换历史记录（MSSWPREC）](configobject/UDG/20.15.2/MSSWPREC.md)

## 使用实例

查询指定微服务主备倒换历史记录。

```
O&M    #1202
%%DSP MSSWPREC:;%%
RETCODE = 0  操作成功

结果如下
------------------------
微服务名称            旧的主实例ID                  旧的主实例所在进程ID                                 旧的主实例所在Pod名称             旧的主实例所在节点ID     新的主实例ID                  新的主实例所在进程ID                             新的主实例所在Pod名称        新的主实例所在节点ID   主实例发生切换的时间       微服务组                           微服务可选项

TICK                  11966105759974351941          sfm-pod-66c689c87d-cj4kf192-168-0-1__110__0          sfm-pod-66c689c87d-cj4kf          192.168.0.1              11966105759974504825          sfm-pod-66c689c87d-klvtn192-168-0-3__110__0      sfm-pod-66c689c87d-klvtn     192.168.0.3            2022-05-17 13:31:52        N/A                                999                 
TICK                  11966105759974351941          sfm-pod-66c689c87d-cj4kf192-168-0-2__110__0          sfm-pod-66c689c87d-cj4kf          192.168.0.2              11966105759974351941          sfm-pod-66c689c87d-cj4kf192-168-0-1__110__0      sfm-pod-66c689c87d-cj4kf     192.168.0.1            2022-05-17 13:31:24        N/A                                999                 
TICK                  11966105759974504821          sfm-pod-66c689c87d-klvtn192-168-0-3__110__0          sfm-pod-66c689c87d-klvtn          192.168.0.3              11966105759974351941          sfm-pod-66c689c87d-cj4kf192-168-0-2__110__0      sfm-pod-66c689c87d-cj4kf     192.168.0.2            2022-05-17 12:57:33        N/A                                999                
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示微服务主实例切换历史记录（DSP-MSSWPREC）_63033396.md`
