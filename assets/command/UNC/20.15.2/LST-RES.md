---
id: UNC@20.15.2@MMLCommand@LST RES
type: MMLCommand
name: LST RES（查询资源配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RES
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 资源管理
- 资源实例管理
status: active
---

# LST RES（查询资源配置信息）

## 功能

该命令用于查询资源配置信息。用户可用该命令查看资源的名称、类型等配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESNAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：该参数表示资源名称，指节点或容器的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RES]] · 资源信息（RES）

## 使用实例

- 查询所有资源配置信息：
  ```
  LST RES:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  --------
  逻辑资源编号    资源名称    VNFM分配的资源编号    VIM分配的资源编号                       资源实例类型    内存容量（MB）    存储容量（GB）    CPU核数量    HA组    亲和性组    扩展组    主机位置                                主机名称                资源类型    父资源名称

  1               OMU1        NE=34618142           92a109d2-5aef-4f64-8c13-dd625d56aeaf    OMU             16384             546               4            NULL    NULL        NULL      48645528-D21D-B211-88D4-001823E5F68B    S19_RN43_SRN0_Host20    
  容器
        
  nps-omum-node-app-66a8e66e-0

  2               OMU2        NE=34618143           634cc600-486b-484c-a033-bb6ec1729c40    OMU             16384             546               4            NULL    NULL        NULL      4246A128-D21D-B211-AC08-001823E5F68B    S19_RN43_SRN0_Host7     
  容器
        
  nps-omum-node-app-66a8e66e-0

  (结果个数 = 2)
  ---    END
  ```
- 查询名称为OMU1资源配置信息：
  ```
  LST RES: RESNAME="OMU1";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  --------
        逻辑资源编号  =  1
            资源名称  =  OMU1
  VNFM分配的资源编号  =  NE=34618142
   VIM分配的资源编号  =  92a109d2-5aef-4f64-8c13-dd625d56aeaf
        资源实例类型  =  OMU
      内存容量（MB）  =  16384
      存储容量（GB）  =  546
           CPU核数量  =  4
                HA组  =  NULL
            亲和性组  =  NULL
              扩展组  =  NULL
            主机位置  =  48645528-D21D-B211-88D4-001823E5F68B
            主机名称  =  S19_RN43_SRN0_Host20
            资源类型  =  
  容器

          父资源名称  = 
  nps-omum-node-app-66a8e66e-0

  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RES.md`
