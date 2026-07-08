---
id: UNC@20.15.2@MMLCommand@LST NGLANUPNODE
type: MMLCommand
name: LST NGLANUPNODE（查询指定实例名称的UPF节点特征）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGLANUPNODE
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 5G LAN管理
- UP节点管理
status: active
---

# LST NGLANUPNODE（查询指定实例名称的UPF节点特征）

## 功能

**适用NF：SMF**

该命令用于5G LAN场景中查询指定UPF实例对应的UPF节点特征参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| GROUPID | 5G LAN组ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN组的ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是18~37。GROUPID以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A-F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A-F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGLANUPNODE]] · 指定实例名称的UPF节点特征（NGLANUPNODE）

## 使用实例

基于5G Lan组ID和实例名称，查询所有符合条件的UPF节点特征：

```
%%LST NGLANUPNODE: NFINSTANCENAME="upf1", GROUPID="a0000001-460-003-a000000001";%%
RETCODE = 0  操作成功

结果如下
--------
UPF实例名称  5G LAN组ID                   是否支持N6通信  
        
upf1         a0000001-460-003-a000000001  使能                   
(结果个数 = 1)

---    END

%%LST NGLANUPNODE: NFINSTANCENAME="upf1";%%
RETCODE = 0  操作成功

结果如下
--------
UPF实例名称  5G LAN组ID                   是否支持N6通信  

upf1         a0000001-460-003-01          使能            
upf1         a0000001-460-003-a000000001  使能                   
(结果个数 = 2)

---    END

%%LST NGLANUPNODE: GROUPID="a0000001-460-003-a000000001";%%
RETCODE = 0  操作成功

结果如下
--------
UPF实例名称  5G LAN组ID                   是否支持N6通信  

upf1         a0000001-460-003-a000000001  使能            
upf2         a0000001-460-003-a000000001  使能            
(结果个数 = 2)

---    END

%%LST NGLANUPNODE:;%%
RETCODE = 0  操作成功

结果如下
--------
UPF实例名称  5G LAN组ID                   是否支持N6通信  

upf1         a0000001-460-003-01          使能            
upf1         a0000001-460-003-a000000001  使能            
upf2         a0000001-460-003-01          使能            
upf2         a0000001-460-003-a000000001  使能            
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询指定实例名称的UPF节点特征（LST-NGLANUPNODE）_98748905.md`
