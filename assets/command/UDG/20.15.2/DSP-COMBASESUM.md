---
id: UDG@20.15.2@MMLCommand@DSP COMBASESUM
type: MMLCommand
name: DSP COMBASESUM（显示BASE亚健康概况）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: COMBASESUM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 亚健康检测
status: active
---

# DSP COMBASESUM（显示BASE亚健康概况）

## 功能

该命令用于显示Base平面亚健康链路概况。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [BASE亚健康概况（COMBASESUM）](configobject/UDG/20.15.2/COMBASESUM.md)

## 使用实例

显示BASE平面亚健康链路概况：

```
%%DSP COMBASESUM;%% RETCODE = 0 操作成功 

结果如下 
------------------------ 
源端节点ID   源端POD ID                                 总链路数 亚健康链路数 最小亚健康度 最大亚健康度 平均亚健康度 
10.19.55.187 sfm-pod-668cbc4b6c-fw2lb10-111-0-29       33        3            83            275           161
10.19.15.149 sfm-pod-668cbc4b6c-x7wzg10-111-0-114      55        3            125           325           200
10.19.15.149 haf-pod-5pd5s10-111-0-122                 55        3            183           308           227
10.19.55.187 haf-pod-4r2kh10-111-0-20                  54        3            83            308           169
10.19.55.142 haf-pod-2s9rx10-111-0-85                  55        3            141           283           196
10.19.35.135 netcssim-pod-596d648f49-8zbrq10-111-1-162 9         6            116           166           138
10.19.55.100 appctrl-pod-79c7dcb787-5g4cc10-111-1-200  25        3            108           300           180
10.19.35.135 srvcssim-pod-546c584965-zxclq10-111-1-174 9         6            91            200           153
(结果个数 = 8)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示BASE亚健康概况（DSP-COMBASESUM）_97800864.md`
