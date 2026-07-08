---
id: UNC@20.15.2@MMLCommand@LST NGPRDREGTIMEDNN
type: MMLCommand
name: LST NGPRDREGTIMEDNN（查询基于DNN的周期性注册时长配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPRDREGTIMEDNN
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM协议参数管理
- 5G移动管理定时器
status: active
---

# LST NGPRDREGTIMEDNN（查询基于DNN的周期性注册时长配置）

## 功能

**适用NF：AMF**

该命令用于查询基于DNN的周期性注册时长配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNNI | DNN网络标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定周期性注册时长的目标DNN网络标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>- “*”表示通配符，如果DNNNI为“*”，表示所有DNNNI都支持此配置的周期性注册时长。<br>- 使用DNNNI参数的配置值在用户签约数据smfSelData中所有切片下的DNN列表中进行匹配。 |

## 操作的配置对象

- [基于DNN的周期性注册时长配置（NGPRDREGTIMEDNN）](configobject/UNC/20.15.2/NGPRDREGTIMEDNN.md)

## 使用实例

查询DNNNI为“abc”的配置，执行如下命令：

```
%%LST NGPRDREGTIMEDNN:DNNNI="abc";%%
RETCODE = 0  操作成功

输出结果如下
------------------------
           DNN网络标识  =  ABC
周期性注册时长获取策略  =  本地配置优先
            T3512(min)  =  780
   移动可达定时器(min)  =  792
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于DNN的周期性注册时长配置（LST-NGPRDREGTIMEDNN）_75822976.md`
