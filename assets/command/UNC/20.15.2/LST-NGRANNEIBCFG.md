---
id: UNC@20.15.2@MMLCommand@LST NGRANNEIBCFG
type: MMLCommand
name: LST NGRANNEIBCFG（查询NG-RAN基站邻接关系配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGRANNEIBCFG
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- gNodeB邻接关系管理
status: active
---

# LST NGRANNEIBCFG（查询NG-RAN基站邻接关系配置）

## 功能

**适用NF：AMF**

此命令用于查询中手动添加的NG-RAN基站邻接关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGRANNODETYPE | NG-RAN基站类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定中心基站和邻接基站公用的基站类型。<br>数据来源：全网规划<br>取值范围：<br>- “GNB（Global gNB）”：Global gNB<br>- “MACRONGENB（Macro ng-eNB）”：Macro ng-eNB<br>- “SHORTNGENB（Short Macro ng-eNB）”：Short Macro ng-eNB<br>- “LONGNGENB（Long Macro ng-eNB）”：Long Macro ng-eNB<br>- “N3IWF（Global N3IWF）”：Global N3IWF<br>默认值：无<br>配置原则：无 |
| PLMN | PLMN | 可选必选说明：可选参数<br>参数含义：该参数标识接入网设备的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| NGRANNODEID | NG-RAN基站标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定中心NG-RAN基站的标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。如果NGRANNODETYPE设置为GNB，则该参数的值范围为0到4294967295；如果NGRANNODETYPE设置为MACRONGENB，则该参数的值范围为0到1048575；如果将NGRANNODETYPE设置为SHORTNGENB，则该参数的取值范围为0到262143；如果将NGRANNODETYPE设置为LONGNGENB，则该参数的取值范围为0到2097151；如果NGRANNODETYPE被设置为N3IWF，则该参数的值范围从0到65535。<br>默认值：无<br>配置原则：无 |
| NODEIDLEN | NG-RAN基站标识长度(比特) | 可选必选说明：可选参数<br>参数含义：该参数用于指定中心NG-RAN基站和邻接基站共用的标识长度(比特)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是16~32。当NGRANNODETYPE选择GNB时，本参数的输入范围应当是22到32；当NGRANNODETYPE选择MACRONGENB时，本参数应当输入值为20；当NGRANNODETYPE选择SHORTNGENB时，本参数应当输入值为18；当NGRANNODETYPE选择LONGNGENB时，本参数应当输入值为21；当NGRANNODETYPE选择N3IWF时，本参数应当输入值为16。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGRANNEIBCFG]] · NG-RAN基站邻接关系配置（NGRANNEIBCFG）

## 使用实例

- 查询“NG-RAN基站类型”为“Global gNB”的NG-RAN基站邻接关系，执行如下命令：
  ```
  %%LST NGRANNEIBCFG: NGRANNODETYPE=GNB;%%
  RETCODE = 0  操作成功

  结果如下
  --------
            NG-RAN基站类型  =  Global gNB
                      PLMN  =  12303
            NG-RAN基站标识  =  327697
  NG-RAN基站标识长度(比特)  =  24
    邻接NG-RAN基站标识列表  =  327696&327698&327699
  (结果个数 = 1)

  ---    END
  ```
- 查询所有手动添加的NG-RAN基站邻接关系，执行如下命令：
  ```
  %%LST NGRANNEIBCFG:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
            NG-RAN基站类型  =  Global gNB
                      PLMN  =  12303
            NG-RAN基站标识  =  327697
  NG-RAN基站标识长度(比特)  =  24
    邻接NG-RAN基站标识列表  =  327696&327698&327699
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NG-RAN基站邻接关系配置（LST-NGRANNEIBCFG）_09652382.md`
